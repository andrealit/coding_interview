class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        rows, columns = len(matrix), len(matrix[0])
        up = 0
        left = 0
        right = columns - 1
        down = rows - 1
        
        while len(ans) < rows*columns:
            # first row, left to right
            for col in range(left, right + 1):
                ans.append(matrix[up][col])
            
            # last column, down
            for row in range(up+1, down+1):
                ans.append(matrix[row][right])
            
            # different row
            if up != down:
                # go backwards
                for col in range(right-1, left-1, -1):
                    ans.append(matrix[down][col])
            
            # different column
            if left != right:
                # go upwards
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])
            
            # traverse up
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans
        
        