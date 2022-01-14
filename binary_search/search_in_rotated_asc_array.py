# Search the target in the rotated array without duplicates and array is in ascending order.
def search(nums, target):      
    
    def pivot(nums):
        
            start = 0
            end = len(nums)-1

            while start<=end:

                mid = (start+end)//2
                if mid<end and nums[mid] > nums[mid+1]:
                    return mid
                if mid>start and nums[mid] < nums[mid-1]:
                    return mid-1
                if nums[start] < nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
            return -1
    
        
    def agonistic_binary_search(arr, start, end, target):
    
        start = start
        end = end
        
        while start<=end:

            mid = (start+end)//2

            if arr[mid] == target:
                return mid
            
            if arr[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return -1
        

    peak = pivot(nums)
    
    # if there is nopivot that means it is sortes array without any rotation.
    if peak == -1:
        return agonistic_binary_search(nums, 0, len(nums)-1, target)

    left_search  = agonistic_binary_search(nums, 0, peak, target)
    
    if type(left_search) == int and left_search!=-1:
        return left_search
    else:
        return agonistic_binary_search(nums, peak+1, len(nums)-1, target)

print(search([5,1,3],3))