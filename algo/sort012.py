def sort012(arr,n):

    arr.sort() # builtin sort
    #***Using bubble sort
    # temp = 0
    # for i in range(n):
    #     for j in range(i,n):
    #         if arr[i] > arr[j]:
    #             temp = arr[j]
    #             arr[j] = arr[i]
    #             arr[i] = temp
    # return arr

    count = [0, 0, 0]
    for i in range(n) :

        count[arr[i]] += 1

    i = 0

    for j in range(3) :

        while(count[j]) :

            arr[i] = 0 + j
            i += 1
            count[j] -= 1
    return arr

t = int(input())


for _ in range(t):
    n = int(input().strip())

    if n == 0:
        arr ,n = list(), 0
    
    arr = list(map(int, input().strip().split(" ")))

print(sort012(arr,n))
