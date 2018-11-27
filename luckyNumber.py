def check(a):
	
	for j in range(2,len(a)):
		p=1
		for i in range(1,len(a)+1):
		
			if(i%j==0):
		
			#	print("ele",a[i-p])
			#	print("index",i-p)
				del(a[i-p])
				p=p+1;
	#	print(a)
	print(a)


a=[1,4,3,5,7,9,3,6,8,1,2,7,9,0]
check(a)
