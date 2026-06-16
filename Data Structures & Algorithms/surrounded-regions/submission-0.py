class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board


        X = 'X'
        O = 'O'
        V = 'V'

        rows, cols = len(board), len(board[0])
        neighbors = [(0,1),(0,-1),(-1, 0),(1, 0)]

        def dfs(row, col):
            board[row][col] = V

            for r1, c1 in neighbors:
                new_row = row+r1
                new_col = col+c1

                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == O:
                    board[new_row][new_col] = V
                    dfs(new_row, new_col)
        

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0 or row == (rows-1) or col == (cols-1):
                    if board[row][col] == O:
                        dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == O:
                    board[row][col] = X
                if board[row][col] == V:
                    board[row][col] = O
        
        





        