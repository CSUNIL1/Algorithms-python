def sort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1,len(l)):
            if l[j]<l[min_idx]:
                min_idx=j
        l[i],l[min_idx]=l[min_idx],l[i]
    print(l)

l=[9,7,5,3,1,8,6,4,2]
sort(l)
