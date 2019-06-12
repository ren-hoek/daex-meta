import pymongo as py
import gridfs


def get_from_gridfs(d, f):
    """Extract file into gridFS.

    Import an open file into the gridFS of mongo database d.
    Inputs:
        d: Mongo db to extract file from
        f: ObjectId of file
    output:
        b: bytestream of file
    """
    fs = gridfs.GridFS(d)
    b = fs.get(f).read()
    return b


def import_to_gridfs(d, f, n, s=False):
    """Import file into gridFS.

    Import an open file into the gridFS of mongo database d.
    Inputs:
        d: Mongo databd to import into
        f: File stream to import
        n: Filename for gridFS
        s: Boolean bytestream or not
    output:
        b: objectid of imported file
    """
    fs = gridfs.GridFS(d)
    if s == True:
        b = fs.put(f, filename=n)
    else:
        b = fs.put(open(f, 'rb'), filename=n)
    return b


def stream_to_gridfs(d, f, n):
    """Import file bytestream into gridFS.

    Import an open file into the gridFS of mongo database d.
    Inputs:
        d: Mongo databd to import into
        f: File stream to import
        n: Filename for gridFS
    output:
        b: objectid of imported file
    """
    fs = gridfs.GridFS(d)
    b = fs.put(f, filename=n)
    return b


def create_doc(c, d):
    """Create document.

    Create a document in a MongoDB collection.
    Inputs:
        c: MongoDB collection
        d: Document to insert
    Output
        Boolean success indicator
    """
    try:
        c.insert_one(d)
        return True
    except:
        return False


def update_doc(c, i, d, u=False):
    """Update document.

    Update a document within a MongoDB collection.
    Inputs:
        c: MongoDB collection
        i: ObjectId of document to update
        d: Updated document
        u: Create if document doesn't exist
    Output
        Boolean success indicator
    """
    try:
        c.update_one({'_id': i}, {'$set': d}, upsert = u)
        return True
    except:
        return False
