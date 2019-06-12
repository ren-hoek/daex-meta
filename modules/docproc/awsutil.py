import boto3
import json


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


def get_s3_object(s, b, k):
    """Get S3 Object

    Returns an object representing an s3 object.
    The session profile must have permissions on the bucket.
    Input:
        s: A boto3 session
        b: S3 Bucket name
        k: Object key
    Output:
        S3 object
    """
    return s.resource('s3').Object(b, k)


def put_s3_object(s, b, k, f):
    """ Write object to S3.

    Returns a boolean indicating successful write.
    The session profile must have permissions on the bucket.
    Input:
        s: A boto3 session
        b: S3 Bucket name
        k: Object key
        f: file contents
    Output:
        S3 object
    try:
        s.resource('s3').Object(b, k).put(Body=f)
        return True
    except:
        return False
    """
    s.resource('s3').Object(b, k).put(Body=f)
    return True

def read_s3_json(f):
    """Read an S3 json file.

    Returns a dictionary representing a s3 json object.
    Input:
        f: S3 json file object
    Output:
        Dictionary representing S3 json objest.
    """
    return json.loads(f.get()["Body"].read().decode('utf-8'))


def write_dict_json(d):
    """Write a dictionary to JSON.

    Returns a json string representing a dictionary.
    Input:
        d: S3 json file object
    Output:
        Dictionary representing S3 json objest.
    """
    return json.dumps(d)

