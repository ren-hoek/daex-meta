import tempfile
import imgkit
from pyvirtualdisplay import Display
import docproc.pymgutil as pu


def insert_html_images(d):
    """Inserts an image into page images for html content types

    input
        d: ObjectId from pymongo

    output
        Boolean sucess indicator
    """
    client = py.MongoClient('mongo')
    db = client['docs']
    col = db['aug_meta']
    doc_id = d['_id']
    doc = col.find_one({"_id": doc_id})
    html_file = pu.get_from_gridfs(db, doc['raw_file'])
    f = tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.html')
    f.write(html_file)
    f.flush()
    display = Display(visible=0, size=(800,600))
    display.start()
    jpgfile = imgkit.from_file(f.name, 'pageimg.jpg')
  #  display.stop()
    f.delete
    b = py.import_to_gridfs(db, 'pageimg.jpg', 'image')
    if 'page_images' not in doc:
        doc['page_images']=[]
    doc['page_images'].append(b)

    success = pu.update_doc(col, doc_id, doc)

    return success

