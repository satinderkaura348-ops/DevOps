env = ["dev", "stg", "prd"]

is_found = False
key = "testing"
for i in env:
    if i == key:
        is_found = True

    if is_found:
        print("Key found")
        break
    else:
        print("NOPE, Not Found")

