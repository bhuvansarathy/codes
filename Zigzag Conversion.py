class Solution(object):
    def convert(self, s, numRows):
        # Edge case: no zigzagging possible
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize rows
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for char in s:
            rows[current_row] += char
            
            # If we hit the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down
            current_row += 1 if going_down else -1
            
        return "".join(rows)
