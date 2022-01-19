#!/usr/bin/env python
import boto3

BUCKET = 'aua-test-09898'
session = boto3.Session(profile_name='admin')
s3 = session.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()

# if you want to delete the now-empty bucket as well, uncomment this line:
# bucket.delete() 