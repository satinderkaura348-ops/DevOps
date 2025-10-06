import argparse

parser = argparse.ArgumentParser(description = "This script allows you to find which server is currently active")
args = parser.parse_args()


new_server1 = {
        "env": "dev",
        "server": "aws Linux2",
        "ram": 8096,
        "cpu": 4,
        "active": True
        }

new_server2 = {
        "env": "prod",
        "server": "aws linux2",
        "cpu": 8,
        "ram": 10240,
        "active": False
        }

env_details = [new_server1, new_server2]


for env in env_details:
    for key,value in env.items():
            if key == "active" and value == True:
                print(env.values())    

