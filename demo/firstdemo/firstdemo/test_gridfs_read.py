import pymongo
import gridfs
import os.path

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/scrapy')
db=client.scrapy
fs=gridfs.GridFS(db,collection='fs')
collection=db.fs.files



dirs=os.path.dirname(os.path.realpath(__file__))

for row in collection.find({},no_cursor_timeout=True):
    filename=row['filename']
    # md5=row['md5']

    localfile=dirs+'/'+'image'+'/'+os.path.basename(filename)
    os.makedirs(os.path.dirname(localfile),mode=0o777,exist_ok=True)
    with open(localfile,'wb') as f:
        _id=row['_id']

        try:
            gird_out=fs.get(file_id=_id)
            f.write(gird_out.read())
        except Exception as e:
            print(e)
        finally:
            if gird_out:
                pass
