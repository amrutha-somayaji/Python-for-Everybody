def computepay(h,r):
	if h>40:
		usual_pay=40*r
		pay_for_extra=1.5*(h-40)*r
		total=usual_pay+pay_for_extra
	else: total=h*r
	return total

hrs = input("Enter Hours: ")
h=float(hrs)

rate = input("Enter Rate: ")
r=float(rate)

pay = computepay(h,r)
print("Pay",pay)