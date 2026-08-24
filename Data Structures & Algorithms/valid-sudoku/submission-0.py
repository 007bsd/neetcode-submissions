class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need three things, rows, cols and box
        rows = set()
        cols = set()
        boxes = set()
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                row_key = (row, value)
                col_key = (col, value)
                band = row //3
                stack = col //3
                box_number = (band * 3) + stack
                box_key = (box_number, value)
                if row_key in rows:
                    return False
                if col_key in cols:
                    return False
                if box_key in boxes:
                    return False
                rows.add(row_key)
                cols.add(col_key)
                boxes.add(box_key)
        return True