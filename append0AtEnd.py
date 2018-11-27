def c_zero(a,lent):
	'''i=0
	while(i<lent):
		if(a[i]==0):
			temp=a[i]
			j=i+1
			while(j<lent):
				a[j-1]=a[j]
				j=j+1
			a[j-1]=temp
		i=i+1
	return a'''
	start=0
	for i in range(0,lent):
		if(a[i]!=0):
			a[start]=a[i]
			start=start+1
	while(start<lent):
		a[start]=0
		start=start+1
	return a

a=[1,0,2,2,0,4,12]
lent=len(a)
print(lent)
array=c_zero(a,lent)
print(array)

