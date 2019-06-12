import boto3
import os
from rq import Queue
from redis import Redis
import docproc.awsutil as aws
from docproc.docsrch import create_document

redis_conn = Redis(host='redis')
q = Queue(connection=redis_conn)

session = aws.create_session()
rd = os.environ['S3_READ_BUCKET']
wt = os.environ['S3_WRITE_BUCKET']
wt_path = os.environ['S3_WRITE_PATH']

rd_bucket = aws.get_s3_bucket(session, rd)
wt_bucket = aws.get_s3_bucket(session, wt)

jobs = 0
for fl in wt_bucket.objects.filter(Prefix=wt_path):
    if "extracted.json" in fl.key:
        job = q.enqueue(create_document, wt, fl.key)
        jobs = jobs + 1
print("Submitted: " + str(jobs) + " jobs")

