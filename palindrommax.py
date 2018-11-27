def check_palindrom(str1,i,j):
	flag=0
	while(i<j):
		if(str1[i]!=str1[j]):
			flag=1
			break
		i=i+1
		j=j-1
	return flag
	
def palindrom(str1):
	lent=len(str1)
	i=0
	j=1
	max1=0
	while(i<lent):
		if(str1[i]==str1[j]):
			flag=check_palindrom(str1,i,j)
			if(flag==0):
				count=0
				k=i
				for i in range(i,j+1):
					print(str1[i],end="")
					count=count+1
				print()
				
				if(count>max1):
					max1=count
					s=k
					p=j
			i=j+1
			j=i+1
			if(i>=lent and j>=lent):
				pass
		else:
			j=j+1
			if(j>=lent):
				i=i+1
				j=i+1
			if(i==lent-1):
				pass
	printf(str1,s,p)

def printf(str1,s,p):
	print("max palindrom")
	for i in range(s,p+1):
		print(str1[i],end="")
	print()
str1="abbacdfabbbaaa"
palindrom(str1)
