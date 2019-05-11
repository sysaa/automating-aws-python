import boto3
import click

session = boto3.Session(profile_name='root')
s3 = session.resource('s3')

@click.group()
def cli():
	"Webotron deploys websites to AWS"
	pass

@cli.command('list_buckets')
def list_buckets():
	"List all S3 buckets"
	for bucket in s3.buckets.all():
		print(bucket)

@cli.command('list_buckets_objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
	"List all S3 bucket objects"
	for obj in s3.Bucket(bucket).objects.all():
		print(obj)


if __name__ == '__main__':
	cli()
