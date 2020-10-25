"""
Runtime: 32 ms
Memory: 14.5 MB
"""

class Solution:        

    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
    """

    def generateParenthesis(self, n):
        res = []
        self.dfs(n, n, "", res)
        return res
            
    def dfs(self, leftRemain, rightRemain, path, res):

        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return  # backtracking
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
            return 
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)


if __name__ == "__main__":

    result = Solution()
    n = 4
    print(result.generateParenthesis(n))
