class Solution:
    def live_neighbors(self, row, col, rows, cols, grid):

        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Make sure to count the center cell located at grid[row][col]
                if not (i == 0 and j == 0):
                    # Using the modulo operator (%) the grid wraps around
                    sum += grid[((row + i) % rows)][((col + j) % cols)]  # looked up
        return sum

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Time complexity : O(m*n)
        # The entire matrix traversed once

        # Space cmplexity : O(m*n)
        # The new board has the space equivalent to current cell, m*n

        '''
        The program does not work on leet code
        I think the program fails at some cases because the live values are wrong

        First daw the rough working of the problem, we must check all eight neighbours,
        Then get the live number  and apply conditions in the problem

        '''

        # if len(board) == 0 || board[0].length == 0 || board = None:
        if len(board) == 0:
            return []

        row = len(board)
        col = len(board[0])
        new_board = [[0 for i in range(col)] for j in range(row)]
        print(new_board)

        for r in range(row):  # execute r times
            for c in range(col):  # excutes c times

                live = self.live_neighbors(r, c, row, col, board)
                print(r, c, live)
                if live < 2 or live > 3:  # under or over population
                    new_board[r][c] = 0

                elif live == 3 and board[r][c] == 0:  # reproduce
                    new_board[r][c] = 1
                else:
                    new_board[r][c] = board[r][c]  # next gen

            print(new_board)

