#!/bin/bash


src=$1
dest=$2
timestamp=$( date '+%y_%m_%d_%H_%M' )

zip -r "$dest/backups-$timestamp.zip" $src > /dev/null
aws s3 sync $dest s3://backup-s3-bucket123/backup/

echo "*****Backup Completed*****"
