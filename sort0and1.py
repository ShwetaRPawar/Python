
def sort(a):
    size=len(a)
    i=0
    mid=int(size/2)
    for i in range(0,mid):
        j=size-1
        while(i<j):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                break
            j=j-1

    return a



a=[0,1,0,1,1]
a=sort(a)
print(a)
