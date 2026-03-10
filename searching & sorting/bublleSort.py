def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr=[5,4,8,3,2,1]
sorted_list=bubble_sort(arr)
print(sorted_list)