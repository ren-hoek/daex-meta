import boto3
import os
from rq import Queue
from redis import Redis
import docproc.awsutil as aws
from docproc.mgtika import insert_doc

redis_conn = Redis(host='redis')
q = Queue(connection=redis_conn)

session = aws.create_session()
rd = os.environ['S3_READ_BUCKET']
wt = os.environ['S3_WRITE_BUCKET']
rd_path = os.environ['S3_READ_PATH']
rd = 'coconut-zero'
wt = 'coconut-zero-writable'
rd_path = 'million/'
col = os.environ['COLLECTION']
rd_bucket = aws.get_s3_bucket(session, rd)

jobs = 0
for fl in rd_bucket.objects.filter(Prefix=rd_path):
    job = q.enqueue(insert_doc, rd, fl.key, col)
    jobs = jobs + 1
print("Submitted: " + str(jobs) + " jobs")

