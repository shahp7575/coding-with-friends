"""
Runtime: 696 ms
Memory: 15.3 MB
"""

from typing import List

class Solution:

    """
    Problem #77 Combinations

    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    You may return the answer in any order.

    Input: n = 4, k = 2
    Output:
    [
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
    ]
    """

    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        n = [i for i in range(1, n+1)]
        self.len = len(n)
        self.k = k
        self.dfs(n, [], res)
        return res

    def dfs(self, n, path, res):

        if len(path) == self.k and path not in res:
            res.append(path)
            path = path[1:]


        for i in range(len(n)):

            if i > 0 and len(n) == self.len:
                break

            self.dfs(n[i+1:], path + [n[i]], res)            
        

if __name__ == "__main__":

    result = Solution()
    n = 4
    k = 2
    print(result.combine(n, k))