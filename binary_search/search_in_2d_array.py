# Search in the 2D array rows and columns are in ascending order.
def searchMatrix(matrix, target):
        
    row = 0
    col = len(matrix[0])-1
    
    while row<len(matrix) and col>=0:
        
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col = col-1
        else:
            row = row+1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],300))