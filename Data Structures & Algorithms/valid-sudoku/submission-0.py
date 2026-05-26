class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == '.':
                    continue

                box = (r//3)*3 + (c//3)

                if ele in rows[r] or ele in cols[c] or ele in boxs[box]:
                    return False

                rows[r].add(ele)
                cols[c].add(ele)
                boxs[box].add(ele)

        return True
        