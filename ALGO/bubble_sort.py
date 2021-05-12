def bubblesort(arr, n):
    count = 0
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                count += 1

    print(count)


n = int(input())
arr = input().split()
bubblesort(arr, n)