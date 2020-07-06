# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
	caps=line.upper()
	caps=caps.rstrip()
	print(caps)