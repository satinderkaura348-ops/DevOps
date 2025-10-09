import os
import datetime
import shutil

def backup_files(source,destination):
	today = datetime.date.today()
	backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")
	shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)

source = "/home/ubuntu/devops/DevOps/roadmap_to_devops/python_for_noobs"
destination = "/home/ubuntu/devops/DevOps/roadmap_to_devops/python_for_noobs/backups"
backup_files(source,destination)
