names = ["first", "second", "third"]
n =input("search for a number: ")

for m in names:
	if n == m:
		print("Found: {}".format(m))
