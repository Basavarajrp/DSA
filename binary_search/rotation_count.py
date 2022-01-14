# Find the Rotation Count in the Rotated Sorted array.
# Same as finding the pivot+1
def array_rotation(array):

    start = 0
    end = len(array)-1

    while start<=end:

        mid  = (start+end)//2

        if mid<end and  array[mid] > array[mid+1]:
            return mid+1
        if mid>start and array[mid] < array[mid-1]:
            return (mid-1)+1
        if array[start] > array[mid]:
            end = mid-1
        else:
            start = mid+1

    return 0

print(array_rotation([4,0,1,2,3]))