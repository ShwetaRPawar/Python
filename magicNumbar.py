def magic(num):
	original=num
	sum1=0
	sum2=0
	while(num!=0):
		rem=num%10
		sum1=sum1+rem
		num=int(num/10)
	op=sum1
	while(op!=0):
		rem=op%10
		sum2=(sum2*10)+rem
		op=int(op/10)
	mul=sum1*sum2
	if(mul==original):
		print(mul,"is magic number")
	else:
		print(mul,"is not magic number")

num=1729
print(num)
magic(num)
