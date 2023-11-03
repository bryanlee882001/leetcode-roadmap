

#2 Search a 2D Matrix
def searchMatrix(matrix, target):

    row = 0 

    while row <= (len(matrix)-1):
        
        if matrix[row][len(matrix[row])-1] == target: 
            return True 
        
        elif matrix[row][len(matrix[row])-1] < target: 
            row += 1 
            continue 
        
        else: 
            left = 0 
            right = len(matrix[row])-1

            while left <= right: 

                mid = (left + right)//2 

                if matrix[row][mid] > target:
                    left = mid + 1 

                elif matrix[row][mid] < target:
                    right = mid - 1

                elif matrix[row][mid] == target:
                    return True

            row += 1 
        
    return False
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
# target = 13
# print(searchMatrix(matrix,target)) 


def minEatingSpeed(piles,h):
    pass



piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))