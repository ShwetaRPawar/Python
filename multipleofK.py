	
def multiple(a,k):
    temp=[]
    for i in range(0,len(a)):
        s=int(k)/int(a[i])
        if s in temp:
            print(a[i],int(s))
        else:
            temp.append(a[i])
	



array=[2,4,1,6,5,40,1]
print(array)
k=input("k=")
multiple(array,k)

