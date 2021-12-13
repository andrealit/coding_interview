class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

    def setZerosBetter(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # using a flag approach
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # if we find an element that is zero, set the first element to 0
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # iterate the array once again and update
        for i in range(1, R):
            for j in range(1, C): 
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        # check first row
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        
        # check the first column
        if is_col:
            for i in range(R):
                matrix[i][0] = 0