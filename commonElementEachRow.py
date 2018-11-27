def comman(a):
	dic={}
	count=-1
	for i in range(0,len(a)):
		for j in range(0,len(a[i])):
			if(a[i][j] not in dic):
				count=count+1
				dic[a[i][j]]=count
				count=-1
			else:
				for key,value in dic.items():
					if (a[i][j]==key):
						if(value==i):
							pass
						else:
							value=value+1
							dic[key]=value
	for key,value in dic.items():
		if(value==(len(a)-1)):
			print(key)
				
				
			



a=[[1,2,3,1],
   [2,3,1,4],
   [5,1,8,2]]
print(a)
comman(a)
