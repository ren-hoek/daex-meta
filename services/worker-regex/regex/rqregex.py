import os
import pymongo as py
from rq import Queue
from redis import Redis
import docproc.awsutil as aws
from docproc.docsrch import extract_postcode
import time

start_time = time.time()

redis_conn = Redis(host='redis')
q = Queue(connection=redis_conn)

client = py.MongoClient('mongo')
db = client['docs']
col = db['greenbook']

s3_write_bucket = os.environ['S3_WRITE_BUCKET']

jobs = 0
runs = 1000
for run in range(runs):
    for doc in col.find({},{}):
        job = q.enqueue(extract_postcode, doc, s3_write_bucket)
        jobs = jobs + 1
print("Submitted: " + str(jobs) + " jobs")
elapsed_time = time.time() - start_time
print("submission time:", elapsed_time)

