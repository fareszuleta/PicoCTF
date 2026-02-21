import hashlib

PW = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

key = "1b18e1316f9218cc5b053e1cea28e02e"

for pw in PW:
	hashed = hashlib.md5(pw.encode()).hexdigest()
	if hashed == key:
		print(pw)
		break
