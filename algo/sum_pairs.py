def pairSum(arr, s):
    # Write your code here.
    arr.sort()
    indices = []
    x = len(arr)
    for i in range(x):
        for j in range(i+1,x):
            if arr[i] + arr[j] == s:
                indices.append([arr[i],arr[j]])
    return sorted(indices)
    
        

arr = []
n ,target = input().split()
for _ in range(int(n)):
    arr.append(int(input()))
    

print(pairSum(arr,int(target)))


