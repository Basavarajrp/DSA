def searchRange(nums, target):
    
    def elem_index(array, target, first_index):
        
        start = 0
        end = len(array)-1
        index = -1
        while start<=end:
            mid = (start+end)//2
            
            if array[mid] == target:
                index = mid
                if first_index:
                    end = mid-1
                else:
                    start = mid+1
            
            elif array[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return index
    
    return [elem_index(nums, target, True), elem_index(nums, target, False)]
print(searchRange([5,7,7,8,8,8,8,8,10],8))