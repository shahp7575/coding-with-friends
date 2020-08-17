"""
Incomplete!
"""

from typing import List

class Solution:

    """
    Problem Statement:
    """

    def __init__(self, board, word):
        self.board = board
        self.col = len(board[0])
        self.word = word

    def get_options(self, col, charindex, board):
        
        row_prev = charindex - 1
        row_after = charindex + 1
        col_prev = charindex - col
        col_after = charindex + col

        options = [row_prev, row_after, col_prev, col_after]
        options = [board[i] for i in options if i >= 0]

        return options

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        board = sum(board, [])

        for i in range(len(word)):
            if i != 0:
                try:
                    idx = 
                    print(idx)
                    opts = self.get_options(self.col, board.index(word[i-1]), board)
                except ValueError:
                    return False
            else:
                opts = board
            print(word[i], opts)
            if word[i] in opts:
                print("YES")

if __name__ == "__main__":

    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'SEE'
    result = Solution(board, word)
    print(result.exist(board, word))