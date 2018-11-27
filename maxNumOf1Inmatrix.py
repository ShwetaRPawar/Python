def maximum1(a,n):
	i=0
	j=0
	s=0
	count=0
	temp=[]
	inner=[]
	outer=[]
	hole=[]
	end=int(n)
	end1=int(n)
	sh=(len(a[i]))+1
	sh1=len(a)+1
	while(end1<sh1):
		#print("end1",end1)
		i=0
		end=int(n)
		while(end<sh):	
			n1=n
			k=s
			while(n1!=0):
			
				l=i
				n2=n
				while(n2!=0):
					print(a[k][l],end="")
					if(a[k][l]==1):
						count=count+1
					inner.append(a[k][l])
					l=l+1
					n2=int(n2)-1
				print()
				outer.append(inner)
				inner=[]
				n1=int(n1)-1
				k=k+1
			print()
			hole.append(outer)
			outer=[]
			temp.append(count)
			count=0
			i=i+1
			end=int(end)+1
			
		s=s+1
		end1=int(end1)+1
	maxi=max(temp)
	for i in range(0,len(temp)):
		if(temp[i]==maxi):
			print(hole[i])
		


a=[[1,0,0,0,1,1,0,1],
   [0,1,1,0,0,0,0,1],
   [1,1,0,0,1,1,1,1],
   [0,0,1,1,1,0,1,1],
   [1,1,1,1,1,1,1,1]]
n=input("n:")
maximum1(a,n)
