import boto3
import os

def create_session(p=''):
    """Create boto session.

    Uses values in .aws/credentials and .aws/config.
    Input:
        p: A profile name defined in .aws/config
    Output:
        A boto3 session with the assumed profile role
    """
    if p == '':
        return boto3.session.Session()
    else:
        return boto3.session.Session(profile_name=p)


def get_s3_bucket(s, b):
    """Get S3 bucket.

    Returns an object representing an s3 bucket.
    The session profile must have permissions on the bucket.
    Input:
        s: A boto3 session
        b: S3 Bucket name
    Output:
        S3 bucket object
    """
    return s.resource('s3').Bucket(b)


def download_s3_file(b, k, d):
    """Download S3 file.

    Downloads file from s3 to the local filesystem.
    """
    return b.download_file(k, k.replace(d, ''))


def download_code_from_s3(r, p, w, b, d=''):
    session = create_session(d)
    bucket = get_s3_bucket(session, b)
    repo = r
    package_path = repo + p
    worker_path = repo + w

    if not os.path.exists(p):
        os.makedirs(p)

    for fl in bucket.objects.filter(Prefix=package_path):
        download_s3_file(bucket, fl.key, repo)

    for fl in bucket.objects.filter(Prefix=worker_path):
        download_s3_file(bucket, fl.key, worker_path + "/")

    return True


