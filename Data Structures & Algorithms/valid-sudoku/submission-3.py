class Solution:
    def is_valid(self, line):
        vals = []
        for item in line:
            if item == ".":
                continue
            if item in vals:
                return False
            vals.append(item)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for line in board:
            if not self.is_valid(line):
                return False

        columns = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                columns[i].append(board[j][i])
        for c in columns:
            if not self.is_valid(c):
                return False
        
        sudokus = [[] for _ in range(9)]
        for i in range(9):
            box_row = i // 3
            box_col = i % 3
            for j in range(9):
                row_offset = j // 3
                col_offset = j % 3
                board_row = box_row * 3 + row_offset
                board_col = box_col * 3 + col_offset
                sudokus[i].append(board[board_row][board_col])
        
        for s in sudokus:
            if not self.is_valid(s):
                return False
                
        return True


