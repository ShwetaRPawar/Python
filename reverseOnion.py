def onion(a):
	i=0
	j=0
	k=len(a[i])
	s=len(a)
	n=0
	g=-1
	temp=[]
	while(n<len(a)):
		j=i=n
		while(j<k):
			temp.append(a[i][j])
			#print(a[i][j])
			j=j+1
		k=j=(j-1)
		i=i+1
		while(i<s):
			temp.append(a[i][j])
			#print(a[i][j])
			i=i+1
		s=i=(i-1)
		j=j-1
		if i==n and j==n:
			break
		while(j>g):
			temp.append(a[i][j])
			#print(a[i][j])
			j=j-1
		g=j=(j+1)
		i=i-1
		while(i>n):
			temp.append(a[i][j])
			#print(a[i][j])
			i=i-1
		n=n+1

	temp.reverse()
	print(temp)




a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
onion(a)
