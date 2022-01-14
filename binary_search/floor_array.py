# floor of a number = target element or smallest smaller element in an array
def floor(array,target):

    start = 0
    end = len(array)-1

    # If the given taget number is smaller than the smallest number in the array
    if target < array[start]:
        return False

    while start<=end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return array[end]
print(floor([1,3,5,6,7],0))