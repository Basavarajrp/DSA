# Find the target in the sorted 2d array.
def sorted_2darray(arr, target):

    rows = len(arr) 
    cols = len(arr[0])

    row_start = 0
    row_end = rows-1

    col_mid = (0+(cols-1))//2

    def binary_search(arr, row, col_start, col_end, target):

        while col_start<=col_end:

            mid = (col_start+col_end)//2

            if arr[row][mid] == target:
                return (row, mid)

            if arr[row][mid] > target:
                col_end = mid-1
            else:
                col_start = mid+1
        return False

    if rows == 1:
        return binary_search(arr, 0, 0, cols-1, target)

    # Loop until and unless two rows are remaining
    while row_start < row_end-1:
        
        mid = (row_start+row_end)//2


        if arr[mid][col_mid] == target:
            return (mid,col_mid)
        
        if arr[mid][col_mid]>target:
            row_end = mid
        else:
            row_start = mid

    # # We have two rows at this point
    # start_row = binary_search(arr, row_start, 0, len(arr[row_start])-1, target)
    # if start_row:
    #     return start_row
    # else:
    #     return binary_search(arr, row_end, 0, len(arr[row_end])-1, target)


    # In the case of two rows above condition may take long time it is better to have
    # binary search on the middle col 1st because in the middle col we only have 2 elemnts
    # because of two rows.

    # Check on the 1st row mid element
    if arr[row_start][col_mid] == target:
        return (row_start,col_mid)
    # Check on the 2nd row mid element
    if arr[row_start+1][col_mid] == target:
        return (row_start+1,col_mid)

    # Check on the left part of the row1 by applying the binary search
    if target<=arr[row_start][col_mid-1]:
        return binary_search(arr, row_start, 0, col_mid-1, target)
    # Check on the right part of the row1 by applying the binary search
    if target>=arr[row_start][col_mid+1] and target<= arr[row_start][cols-1]:
        return binary_search(arr, row_start, col_mid+1, cols-1, target)
    # Check on the left part of the row2 by applying the binary search
    if target<=arr[row_start+1][col_mid-1]:
        return binary_search(arr, row_start+1, 0, col_mid-1, target)
    # Check on the right part of the row2 by applying the binary search
    if target>=arr[row_start+1][col_mid+1]:
        return binary_search(arr, row_start+1, col_mid+1, cols-1, target)

print(sorted_2darray([[1,2,3],[4,5,6],[7,8,9]],19))