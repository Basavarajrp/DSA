# Binary search for the descending order
def binary_search_desc(array, target):

    start = 0
    end = len(array)

    while start <= end:
        mid = (start+end)//2
        # Base condition
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            start = mid+1
        else:
            end  = mid-1
    return False
print(binary_search_desc([5,4,3,2,1,0], 7))