import re
import pymongo as py
import docproc.awsutil as aws
import docproc.pymgutil as pu


def find_ukpc(s):
    ukpc = '([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})'
    return [[y for y in x] for x in re.findall(ukpc, s)]


def create_document(b, k):
    """Create mongo document.

    Creates a mongo document from a s3 json file.
    Input:
        f: S3 key
    """
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['greenbook']

    session = aws.create_session()
    s3_obj = aws.get_s3_object(session, b, k)
    success = pu.create_doc(col, aws.read_s3_json(s3_obj))

    return success


def extract_postcode(d, b):
    """Extract Postcode."""
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['greenbook']

    session = aws.create_session()

    doc_id = d['_id']
    doc = col.find_one({"_id": doc_id})
    postcodes = find_ukpc(doc['text'])
    if postcodes:
        doc['postcode'] = postcodes
        pc_key = "testing/" + doc['key'] + "/postcodes.json"
        s3_pc = aws.write_dict_json(postcodes)
        write_s3 = aws.put_s3_object(session, b, pc_key, s3_pc)
        success = pu.update_doc(col, doc_id, doc)
    else:
        success = None

    return success
