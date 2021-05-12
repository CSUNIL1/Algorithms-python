def linear_search(a,key):
    for i in range(len(a)):
        if a[i]==key:
            print("position=",i+1)
            print("index=",i)
            return
    print("number not found")


a=[74,5,8,23,5,1,2,5,6,83,4,55,67,8]
key=int(input("enter number to search:"))
linear_search(a,key)
