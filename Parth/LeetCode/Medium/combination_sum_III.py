"""
Runtime: 36 ms (faster than 44.05%)
Memory: 14.1 MB (less than 99.95%)
"""

from typing import List

class Solution:

    """
    Problem #216:
    Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.
    Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

    Input: k = 9, n = 45
    Output: [[1,2,3,4,5,6,7,8,9]]
    Explanation:
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
    ​​​​​​​There are no other valid combinations.
    """

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        self.k = k
        self.n = n
        nl = [i for i in range(1,10)]
        self.dfs(nl, [], res)
        return res

    def dfs(self, n, path, res):

        if sum(path) == self.n and len(path) == self.k:

            res.append(path)
            return

        if sum(path[-self.k:]) > self.n:

            return

        for i in range(0, len(n)):

            self.dfs(n[i+1:], path + [n[i]], res)


if __name__ == "__main__":

    result = Solution()
    k = 9
    n = 45
    print(result.combinationSum3(k ,n))