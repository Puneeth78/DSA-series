# binary search=same as linear search but array is always sorted in increasing order or decreasing order
def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1

    while start<=end:
        mid=(start+end)//2
        
        if (arr[mid]==target):
            return mid
        
        elif (arr[mid]>target):
            end=mid-1

        elif (arr[mid]<target):
            start=mid+1

    return -1           


arr=[10,20,30,40,50,60,70]
target=80
result=binary_search(arr,target)
print(result)