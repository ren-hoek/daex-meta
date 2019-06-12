import tempfile
import os
from pdf2image import convert_from_path, convert_from_bytes
import docproc.fileutil as fl
import docproc.pymgutil as pu
import pymongo as py


def sorted_ls(p):
    """Order folder list.

    Orders a folder content by create date.
    Input:
        p: Path to folder
    Output:
        List of sorted filenames
    """
    ctime = lambda f: os.stat(os.path.join(p, f)).st_ctime
    return list(sorted(os.listdir(p), key=ctime))


def create_pdf_images(p, f, b=False):
    """Create images from PDF.

    Create jpg images from either a PDF file or bytestream.
    Inputs:
        p: File to convert
        f: Folder to put jpg images in
        b: Bytes IO (Boolean)
    Output:
        List of PIL images of the pages

    """
    if b == False:
        return convert_from_path(p + ".pdf", output_folder = f, fmt='jpg')
    else:
        return convert_from_bytes(p, output_folder = f, fmt='jpg')


def import_page_images(d, p, f, o=True):
    """Import page images to GridFS.

    Convert and import pages images into GridFS.
    Inputs:
        d: Mongo database
        p: File to convert
        f: Folder to get jpg images from
        o: Office file (Boolean)
    Output:
        image_list: List of ObjectIds for GridFS files
    """
    if o == True:
        libre_com = (
            "soffice --headless --convert-to pdf:writer_pdf_Export " + p + " --outdir /tmp"
        )
        os.system(libre_com)
        images = create_pdf_images(p, f)
    else:
        images = create_pdf_images(p, f, True)

    image_list = [pu.import_to_gridfs(d, f + "/" + n, n) for n in sorted_ls(f)]
    return image_list


def insert_pdf_images(d):
    """Insert TIKA extracted metadata and content."""
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['aug_meta']

    temp_dir = tempfile.mkdtemp()

    doc_id = d['_id']
    doc = col.find_one({"_id": doc_id})
    pdf_file = pu.get_from_gridfs(db, doc['raw_file'])

    images = import_page_images(db, pdf_file, temp_dir, False)
    doc['page_images'] = images
    success = pu.update_doc(col, doc_id, doc)

    fl.clean_temp_files(temp_dir)

    return success


def insert_office_images(d):
    """Insert TIKA extracted metadata and content."""
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['aug_meta']

    temp_dir = tempfile.mkdtemp()

    doc_id = d['_id']
    doc = col.find_one({"_id": doc_id})
    pdf_file = pu.get_from_gridfs(db, doc['raw_file'])

    f = tempfile.NamedTemporaryFile(mode='wb', delete=False)
    f.write(pdf_file)
    images = import_page_images(db, f.name, temp_dir, True)
    doc['page_images'] = images
    success = pu.update_doc(col, doc_id, doc)

    fl.clean_temp_files(temp_dir, f.name)

    return success

