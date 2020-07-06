counting=dict()

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
	if not line.startswith('From '): continue
	splitting=line.split()
	time=splitting[5]

	#splitting to get only hours from the time
	hours=time.split(':')
	hour=hours[0]

	#making dict. of the hours
	counting[hour]=counting.get(hour,0)+1

#printed out the key and value from sorted dictionary
for k,v in sorted(counting.items()):
	print(k, v)

	


