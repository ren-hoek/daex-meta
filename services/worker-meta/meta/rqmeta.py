import boto3
import os
from rq import Queue
from redis import Redis
import docproc.awsutil as aws
from docproc.mgtika import insert_meta
import time

start_time = time.time()

redis_conn = Redis(host='redis')
q = Queue(connection=redis_conn)

session = aws.create_session()
rd = os.environ['S3_READ_BUCKET']
wt = os.environ['S3_WRITE_BUCKET']
rd_path = os.environ['S3_READ_PATH']
col = os.environ['COLLECTION']
rd_bucket = aws.get_s3_bucket(session, rd)

jobs = 0
runs = 1
for run in range(runs):
    for fl in rd_bucket.objects.filter(Prefix=rd_path):
        job = q.enqueue(insert_meta, rd, fl.key, col)
        jobs = jobs + 1
print("Submitted: " + str(jobs) + " jobs")
elapsed_time = time.time() - start_time
print("submission time:", elapsed_time)

