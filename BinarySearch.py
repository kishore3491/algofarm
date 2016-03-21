# Binary Search for index of an element in a sorted array
# Time Complexity: O(LogN); N = number of elements in array 
def findIndex(arr, ele):
    alen = len(arr)
    if(alen < 1):
        return -1
    return findIndexHelper(arr, ele, 0, alen)
    
def findIndexHelper(arr, ele, low, high):
    if(low > high):
        return -1
    mid = int((low + high)/2)
    if(arr[mid] == ele):
        return mid
    elif(arr[mid] < ele):
        return findIndexHelper(arr, ele, mid+1, high)
    else:
        return findIndexHelper(arr, ele, low, mid - 1)
    
# Sample input parser from command line
V = int(input().strip())
n = int(input().strip())

ar = [int(x) for x in input().strip().split(' ')]

print(findIndex(ar, V))  
