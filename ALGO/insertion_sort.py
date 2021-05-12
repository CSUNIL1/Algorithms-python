def sort(l):
    n=len(l)
    for i in range(1,n):
        curr_val=l[i]
        posi=i
        while posi>0 and l[posi-1]>curr_val:
            l[posi-1],l[posi]=l[posi],l[posi-1]
            posi-=1
    print(l)

l=[9,7,5,3,1,8,6,4,2]
sort(l)
