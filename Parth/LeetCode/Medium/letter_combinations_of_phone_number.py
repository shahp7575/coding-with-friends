from typing import List

class Solution:

    """

    """

    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        self.dig_dict = {
            '2': ["a", "b", "c"],
            '3': ["d", "e", "f"],
            '4': ["g", "h", "i"],
            '5': ["j", "k", "l"],
            '6': ["m", "n", "o"],
            '7': ["p", "q", "r", "s"],
            '8': ["t", "u", "v"],
            '9': ["w", "x", "y", "z"]
        }
        self.dig_list = [self.dig_dict[d] for d in digits]
        self.dfs(digits, [], res)
        return res

    def dfs(self, digits, path, res):

        print("digi", digits)

        if path not in res and len(path) == 2:
            res.append(path)

        for i in range(len(self.dig_list)):

            self.dfs(self.dig_list[i+1:], self.dig_list[i][i], res)

    
if __name__ == "__main__":

    result = Solution()
    digits = "23"
    print(result.letterCombinations(digits))