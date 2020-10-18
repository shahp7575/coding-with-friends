"""
Runtime: 32 ms
Memory: 14 MB
"""

from typing import List

class Solution:

    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    """

    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        res = []
        self.dig_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        print(self.dig_dict[digits[0]])
        self.dfs(digits, "", res)
        return res

    def dfs(self, digits, path, res):

        if not digits:
            res.append(path)
            return

        for i in self.dig_dict[digits[0]]:

            self.dfs(digits[1:], path + i, res)
    
if __name__ == "__main__":

    result = Solution()
    digits = ""
    print(result.letterCombinations(digits))