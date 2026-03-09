# linear search=it search the each element in a list one by one until it found the target element

def linear_search(arr,target):
    size=len(arr)
    for i in range(0,size):
        if arr[i]==target:
            return i
    return -1


arr=[10,50,30,40,52,80]
target=30
result=linear_search(arr,target)
print(result)