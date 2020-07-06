# Use the file name mbox-short.txt as the file name
added=0
count=0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
    
#extracting floating values
	pos=line.find(':')
	num=line[pos+2:]
	fnum=float(num)

#for finding average
	added=added+fnum
	count=count+1

avg=added/count
print("Average spam confidence:",avg)
