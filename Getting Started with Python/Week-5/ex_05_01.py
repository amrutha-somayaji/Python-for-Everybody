hrs= input("Enter hours: ")
rate= input("Enter rate: ")
h=float(hrs)
r=float(rate)
pay=r*h
if h>=40:
	extra=h-40
	nor=r*extra
	total=1.5*nor+(40*r)
	print(total)
else:print(pay)