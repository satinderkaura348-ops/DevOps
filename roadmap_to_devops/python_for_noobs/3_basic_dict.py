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



set1 = {}

set2 = {1,2}

set3 = {
        "a": "1",
        "b": "2",
        "c": "hmm"}

print(type(set1))
print(type(set2))
print(type(set3))

list_of_env = ["dev", "stg", "prd", "tst", "qa", "qa", "dev"]
print(list_of_env)

list_of_env = list(set(list_of_env))
print(list_of_env)
