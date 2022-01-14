# Find in Mountain Array(Leet Code)
def mountain_array(arr, target):

    # Finding the peak of the array
    def peak_element(arr):

        start = 0
        end = len(arr)-1

        while start!=end:

            mid = (start+end)//2

            if arr[mid]>arr[mid+1]:
                end = mid
            elif arr[mid]<arr[mid+1]:
                start = mid+1
        return start
    
    # Order agonostic binary search
    def agnostic_binary_search(array, start, end, target):

        start = start
        end = end
        asc = array[0]<array[end]
        while start<=end:
            mid = (start+end)//2
            if array[mid] == target:
                return mid
            
            if asc:
                if array[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if array[mid] > target:
                    start = mid+1
                else:
                    end = mid-1
        return False

    # peak value
    peak = peak_element(arr)

    left_search = agnostic_binary_search(arr, 0, peak, target)
    if type(left_search) == int:
        return left_search
    return agnostic_binary_search(arr, peak, len(arr)-1,  target)

print(mountain_array([1,2,3,4,7,6,4,3,2,1],4))