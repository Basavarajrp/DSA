# Find the peak element in the array with 1st half sorted in ascending order
# and the second half is sorted in the descending order
def peakIndexInMountainArray(arr):
    
    start = 0
    end = len(arr)-1
    
    while start!=end:
        
        mid = (start+end)//2
        
        if arr[mid] > arr[mid+1]:
            end = mid
        elif arr[mid] < arr[mid+1]:
            start = mid+1
    return start
print(peakIndexInMountainArray([0,1,2,3,5,4,3,2,1]))