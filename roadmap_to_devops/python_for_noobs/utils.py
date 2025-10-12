
def linear_search(env, key):
	is_found = False
	for i in env:
		if i == key:
			is_found = True
	return is_found

