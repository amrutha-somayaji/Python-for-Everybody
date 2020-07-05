min=None
max=None
while True:
	number=input('Enter a number: ')

	if number=='done':
		print('Maximum is',int(max))
		print('Minimum is',int(min))
		break

	try:
		fnum=float(number)
	except:
		print('Invalid number')
		continue

	if max is None:
		max=fnum
	elif fnum>max:
		max=fnum

	if min is None:
		min=fnum
	elif fnum<min:
		min=fnum

	

