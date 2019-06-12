import s3cdcp as s3
import os

from redis import Redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

redis_conn = Redis(host='redis')

s3.download_code_from_s3(
    'repos/k8s-data-science/',
    'docproc',
    'worker-regex/regex',
    os.environ['S3_WRITE_BUCKET'],
    os.environ['PROFILE']
)

if __name__ == '__main__':
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()
