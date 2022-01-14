# Order Agnostic Binary search
def order_agnostic_binary_search(array, target):

    start = 0
    end = len(array)-1
    is_acc = array[0] < array[end]

    while start <= end:
        mid = (start+end)//2
        # Base Condition
        if array[mid]==target:
            return mid
        if is_acc:
            if array[mid] > target:
                end = mid-1
            else:
                start = mid+1
        else:
            if array[mid] > target:
                start = mid+1
            else:
                end = mid-1
print(order_agnostic_binary_search([6,5,4,3,2,1],5))