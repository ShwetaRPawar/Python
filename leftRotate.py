def rotate(a,n):

    while(n>0):
        temp=a[0]
        print(temp)
        i=1
        while(i<len(a)):
            a[i-1]=a[i]
            i=i+1
        a[len(a)-1]=temp
        n=n-1
    return a

a=[1,2,3,4,5]
d=1
print(d)
arr=rotate(a,d)
print(arr)
