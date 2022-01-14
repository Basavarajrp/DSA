# Find the target element in the infinity sorted array(means avoid using the len function)
def inif_sorted(array, target):

    start = 0
    end = 1
    while target>array[end]:
        start = end+1
        end = end*2
    
    def index(start, end, target):
        while start <= end:
            mid = (start+end)//2
            if array[mid] == target:
                return mid
            if array[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return False
    return index(start, end, target)
print(inif_sorted([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],13))
