def matrix(a):
    i=0
    j=0
    while(j<len(a[i])):
        k=i
        l=j
        while(k<len(a) and l!=-1):
            print(a[k][l],end=' ')
            k=k+1
            l=l-1
        j=j+1
        print()

    j=j-1
    i=1
    while(i<len(a)):
        k=i
        l=j
        while(k<len(a) and l!=-1):
            print(a[k][l],end=' ')
            k=k+1
            l=l-1
        print()
        i=i+1




a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a)
matrix(a)
