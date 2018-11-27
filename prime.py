def prime(a):
	temp=[]
	for i in range(0,len(a)):
		flag=0
		for  j in range(2,int(a[i]/2)+1):
			if(a[i]%j==0):
				flag=1
				break
		if(flag==0):
			print(a[i])
			

a=[2,4,3,5,6,8,7,11]
prime(a)
