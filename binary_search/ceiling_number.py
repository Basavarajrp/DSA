# Ceiling number = target element or smallest greater element in an array
def ceiling_number_asc(array, target):
    start = 0 
    end = len(array)-1
    
    # If the given taget number is greater than the greatest number in the array
    if target > array[end]:
        return False
    
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid]>target:
            end = mid-1
        elif array[mid]<target:
            start = mid+1
    return array[start]
print(ceiling_number_asc([2,3,5,9,14,16,18], 15))
