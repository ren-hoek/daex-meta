import s3cdcp as s3
import os

s3.download_code_from_s3(
    'repos/k8s-data-science/',
    'docproc',
    'worker-regex/regex',
    os.environ['S3_WRITE_BUCKET'],
    os.environ['PROFILE']
)

os.system("python3 " + os.environ['SUBMIT'] + ".py")

