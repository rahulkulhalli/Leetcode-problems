class Solution:

    def vectorValidate(self, vector):
        encountered = set()

        # No element is valid.
        encountered.add('.')

        min_tol = 1
        max_tol = 9
        parity = True

        for num in vector:
            if num != ".":
                int_num = int(num)
                if num in encountered or int_num < min_tol or int_num > max_tol:
                    parity = False
                    break
                encountered.add(num)

        return parity
    
    def blockValidate(self, block):
        # Flatten to a vector.
        return self.vectorValidate(sum(block, []))

    def getColumn(self, board, ix):
        # collect the ix'th item from every row
        column = []
        for row in board:
            column.append(row[ix])
        
        return column

    def getBlock(self, board, ix):
        block_ix = {
            0: [0, 3],
            1: [0, 3],
            2: [0, 3],
            3: [3, 6],
            4: [3, 6],
            5: [3, 6],
            6: [6, 9],
            7: [6, 9],
            8: [6, 9]
        }

        rows = board[block_ix[ix][0]:block_ix[ix][1]]

        if ix in [0, 3, 6]:
            return [r[:3] for r in rows]
        elif ix in [1, 4, 7]:
            return [r[3:6] for r in rows]
        else:
            return [r[6:] for r in rows]


    def isValidSudoku(self, board):
        all_flags = []

        # First validate rows.
        for row_ix in range(len(board)):
            all_flags.append(self.vectorValidate(board[row_ix]))
        
        # Now validate columns.
        for ix in range(len(board)):
            all_flags.append(self.vectorValidate(self.getColumn(board, ix)))
        
        # Iterate over blocks.
        for row_ix in range(len(board)):
            block = self.getBlock(board, row_ix)
            all_flags.append(self.blockValidate(block))
            
        return all(all_flags)


if __name__ == "__main__":
    board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
            ]
    
    print(Solution().isValidSudoku(board1))
    
    board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]
            ]
    
    print(Solution().isValidSudoku(board2))
    
    board3 = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."]
        ]
    
    print(Solution().isValidSudoku(board3))