# Binary search(Sorted Array in asscending order)
def binary_search_ass(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end)//2
        # Base Condition
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1

    return False
print(binary_search_ass([-1,0,1,2,3,4,5,6,7], -1))