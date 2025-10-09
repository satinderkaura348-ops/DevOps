import boto3


s3 = boto3.resource('s3') #use the s3 resource
bucket_name = input("Enter the S3 bucket name that you wish to create/or to push backups: ")
region = "ap-southeast-2" # use input function according to your preference for location or hardcode instead of ap-southease
file_name = "/home/ubuntu/devops/DevOps/roadmap_to_devops/python_for_noobs/backups/backup_2025-10-09.tar.gz" #path for the file to be uploaded, use input function to enter path manually while running the script

def bucket_list(s3): #define a function to generate a list of buckets in your s3
	for bucket in s3.buckets.all(): #iterate over existing buckets in s3
		print(bucket.name)

def create_bucket(s3,bucket_name,region): #function to create a new bucket, make sure to call the function, i have commented out for test purposes
	s3.create_bucket(Bucket=bucket_name, #call variable bucket_name here
	CreateBucketConfiguration={
	'LocationConstraint': region # call variable region in here
				}
		)
	print("Bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name): #function for uploading backups to s3 bucket
	data = open(file_name, 'rb') # rb means read in binary
	s3.Bucket(bucket_name).put_object(Key=key_name, Body=data) # aws commands
	print("Backup uploaded successfully")

upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")
# bucket_list(s3)
# create_bucket(s3,bucket_name,region)


