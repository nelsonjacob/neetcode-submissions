class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:

            index = low + (high - low) // 2

            midValue = matrix[index // cols][index % cols]
            if target == midValue:
                return True
            if target < midValue:
                high = index - 1
            else:
                low = index + 1
    
        return False