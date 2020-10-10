"""
DFS Backtracking

Runtime: 108 ms
Memory: 14.1 MB
"""

from typing import List

class Solution:

    """
    Problem #39:
    Combination Sum
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order

    The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.

    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        self.target = target
        self.dfs(candidates, [], res)
        return res

    def dfs(self, candidates, path, res):

        if sum(path) > self.target:
            return

        if sum(path) == self.target:
            res.append(path)
            return

        for i in range(len(candidates)):

            self.dfs(candidates[i:], path + [candidates[i]], res)


if __name__ == "__main__":

    result = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(result.combinationSum(candidates, target))