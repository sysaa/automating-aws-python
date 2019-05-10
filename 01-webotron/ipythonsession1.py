# coding: utf-8
import boto3
session = boto3.Session(profile_name='root')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='automate-aws-python-sysaa-boto3')
new_bucket
for bucket in s3.buckets.all():
    print(bucket)
    
s3_client = session.client('s3')
