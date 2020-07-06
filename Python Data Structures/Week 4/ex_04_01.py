lst=list()
fname = input("Enter file name: ")
fh = open(fname)

#form list of words in the line
for line in fh:
	words=line.split()

	#take each word from line and put to the list
	for word in words:
		if word in lst: continue
		lst.append(word)
lst.sort()
print(lst)
