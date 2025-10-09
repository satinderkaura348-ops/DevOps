import os

def run_shell_command(command):
	print(os.system(command))




run_shell_command("date")
run_shell_command("free -h")


