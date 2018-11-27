def check(a):
	user=0
	appo=0
	while( len(a)!=0):
		maxi=max(a)
		user=user+maxi
		a.remove(maxi)
		if(len(a)!=0):
			maxi1=max(a)
			appo=appo+maxi1
			a.remove(maxi1)
	print(user)
	print(appo)
	if(user>appo):
		print("user")
	else:
		print("appo")

a=[2,5,4,6,1,7,8]
print(a)
check(a)
