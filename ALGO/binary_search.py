def bin_search(a,key,f,l):
    mid=(f+l)//2
    if f<=l:
        if a[mid]==key:
            print("position=",mid+1)
            print('index=',mid)
        elif a[mid]>key:
            return bin_search(a,key,f,mid)
        else:
            return bin_search(a,key,mid+1,l)


a=[36,2,3,4,5,6,46,45,79,7,7,6,5,4,3,23,3]
a.sort()
bin_search(a,46,0,len(a)-1)