import pymongo as py
import gridfs
import docproc.fileutil as fl
import docproc.pymgutil as pu
import docproc.awsutil as aws
from tika import unpack


def remove_key_periods(d):
    """Recusively remove periods and dollars from dictionary.

    Steps through the dictionary and removes and periods
    that are in the keys. Mongo won't accept periods in keys
    as thay are special characters.
    Inputs:
        d: Dictionary to step through
    Outputs:
        c: Cleansed dictionary.
    """
    c = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = remove_key_periods(v)
        k = k.replace('$', '')
        c[k.replace('.', '-')] = v
    return c


def standardize_content_type(c):
    """Standardize content type.

    Inputs:
        c: Content Type
    Output:
        Content Type as a list
    """
    return([x.strip() for x in c.split(";")])


def get_tika_content(f):
    """Call TIKA api for rmeta content.

    Calls the rmeta api from TIKA which extracts file metadata
    and content.
    Input:
        f: file object
    Output:
        c: Dictionary of document metadata and content
    """
    try:
        c = remove_key_periods(
            unpack.from_file(f)
        )
        c['success'] = 1
    except:
        c = dict()
        c['success'] = 0
    return c


def get_tika_content_stream(f):
    """Call TIKA api for rmeta content.

    Calls the rmeta api from TIKA which extracts file metadata
    and content.
    Input:
        f: file stream
    Output:
        c: Dictionary of document metadata and content
    """
    try:
        c = remove_key_periods(
            unpack.from_buffer(f)
        )
        c['success'] = 1
    except:
        c = dict()
        c['success'] = 0
    return c


def insert_attachments(d, f, n, c, b, k, s):
    """Insert attachment into Mongo.

    Insert attached documents into metadata collection.
    To extract the metadata the file is passed through Tika.
    Inputs:
        d: Mongo database
        f: Attached file
        p: Attachment name

    """
    col = d[c]
    h = fl.create_sha(f, True)
    meta_exists = [x for x in col.find({'sha1': h}, {})]

    if meta_exists:
        return meta_exists[0]['_id']

    att = get_tika_content_stream(f)
    att['key'] = k + "/attachments/" + n.replace("-", ".")
    att['sha1'] = h
    att['uuid'] = fl.create_uuid()
    write_s3 = aws.put_s3_object(s, b + "-writable", att['key'], f)

    if 'content' in att:
        if att['content'] != "":
            s3_txt = aws.write_dict_json(att['content'])
            write_s3_txt = aws.put_s3_object(s, b +"-writable", att['key'] + "/extracted.json", s3_txt)

    if 'metadata' in att:
        s3_meta = aws.write_dict_json(att['metadata'])
        write_s3_meta = aws.put_s3_object(s, b +"-writable", att['key'] + "/metadata.json", s3_meta)

    c = col.insert_one(att)
    return c.inserted_id


def insert_attachments_meta(d, f, n, c, b, k, s):
    """Insert attachment into Mongo.

    Insert attached documents into metadata collection.
    To extract the metadata the file is passed through Tika.
    Inputs:
        d: Mongo database
        f: Attached file
        p: Attachment name

    """
    col = d[c]
    h = fl.create_sha(f, True)
    meta_exists = [x for x in col.find({'sha1': h}, {})]

    if meta_exists:
        return meta_exists[0]['_id']

    att = get_tika_content_stream(f)
    att['key'] = k + "/attachments/" + n.replace("-", ".")
    att['sha1'] = h
    att['uuid'] = fl.create_uuid()
    write_s3 = aws.put_s3_object(s, b + "-writable", att['key'], f)

    if 'content' in att:
        if att['content'] != "":
            s3_txt = aws.write_dict_json(att['content'])
            write_s3_txt = aws.put_s3_object(s, b +"-writable", att['key'] + "/extracted.json", s3_txt)
            att['content'] = True
        else:
            att.pop('content', None)

    if 'metadata' in att:
        s3_meta = aws.write_dict_json(att['metadata'])
        write_s3_meta = aws.put_s3_object(s, b +"-writable", att['key'] + "/metadata.json", s3_meta)

    c = col.insert_one(att)
    return c.inserted_id


def insert_doc(b, f, c):
    """Insert TIKA extracted metadata and content."""
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db[c]

    session = aws.create_session()
    doc_stream = aws.get_s3_object(session, b, f).get()["Body"].read()

    sha1 = fl.create_sha(doc_stream, True)

    meta_exists = [x for x in col.find({"sha1": sha1}, {"key": True, "_id": False})]

    if meta_exists:
        doc = dict()
        doc['key'] = f
        doc['sha1'] = sha1
        doc['uuid'] = fl.create_uuid()
        doc['duplicate'] = meta_exists[0]['key']
        success = pu.create_doc(col, doc)
        return success

    doc = get_tika_content_stream(doc_stream)
    doc['key'] = f
    doc['sha1'] = sha1
    doc['uuid'] = fl.create_uuid()

    if 'content' in doc:
        if doc['content'] != "":
            s3_txt = aws.write_dict_json(doc['content'])
            write_s3_txt = aws.put_s3_object(session, b +"-writable", doc['key'] + "/extracted.json", s3_txt)

    if 'metadata' in doc:
        s3_meta = aws.write_dict_json(doc['metadata'])
        write_s3_meta = aws.put_s3_object(session, b +"-writable", doc['key'] + "/metadata.json", s3_meta)

    if 'attachments' in doc:
        if doc['attachments'] != []:
            doc['no_attach'] = len(doc['attachments'])
            attachments = doc['attachments']
            doc['attachments'] = [
                insert_attachments(db, attachments.get(x), x, c, b, f, session) for x in attachments
            ]
    success = pu.create_doc(col, doc)

    return success


def insert_meta(b, f, c):
    """Insert TIKA extracted metadata and content."""
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db[c]

    session = aws.create_session()
    doc_stream = aws.get_s3_object(session, b, f).get()["Body"].read()

    sha1 = fl.create_sha(doc_stream, True)

    meta_exists = [x for x in col.find({"sha1": sha1}, {"key": True, "_id": False})]

    if meta_exists:
        doc = dict()
        doc['key'] = f
        doc['sha1'] = sha1
        doc['uuid'] = fl.create_uuid()
        doc['duplicate'] = meta_exists[0]['key']
        success = pu.create_doc(col, doc)
        return success

    doc = get_tika_content_stream(doc_stream)
    doc['key'] = f
    doc['sha1'] = sha1
    doc['uuid'] = fl.create_uuid()

    if 'content' in doc:
        if doc['content'] != "":
            s3_txt = aws.write_dict_json(doc['content'])
            write_s3_txt = aws.put_s3_object(session, b +"-writable", doc['key'] + "/extracted.json", s3_txt)
            doc['content'] = True
        else:
            doc.pop('content', None)

    if 'metadata' in doc:
        s3_meta = aws.write_dict_json(doc['metadata'])
        write_s3_meta = aws.put_s3_object(session, b +"-writable", doc['key'] + "/metadata.json", s3_meta)

    if 'attachments' in doc:
        if doc['attachments'] != []:
            doc['no_attach'] = len(doc['attachments'])
            attachments = doc['attachments']
            doc['attachments'] = [
                insert_attachments_meta(db, attachments.get(x), x, c, b, f, session) for x in attachments
            ]
    success = pu.create_doc(col, doc)

    return success


def insert_content_type(d):
    """Insert content type.

    Inserts a standardized content type list in the
    top level of a document.
    Inputs:
        d: Returned ObjectId dictionary from pymongo find
    Output:
        Boolean sucess indictor
    """
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['aug_meta']

    doc_id = d['_id']
    doc = col.find_one({"_id": doc_id})
    c = doc['metadata']['Content-Type']
    content_type = standardize_content_type(c)
    doc['Content-Type'] = dict()
    doc['Content-Type']['Content'] = content_type[0]
    if len(content_type) == 2:
        doc['Content-Type']['Charset'] = content_type[1]
    success = pu.update_doc(col, doc_id, doc)

    return success

