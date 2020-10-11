"""
Runtime: 116 ms
Memory: 14.1 MB
"""

from typing import List

class Solution:

    """
    Problem #40:
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    Each number in candidates may only be used once in the combination.
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        self.target = target
        self.idx = 0
        self.dfs(candidates, [], res)
        return res

    def dfs(self, candidates, path, res):

        print("Nums -->", candidates)
        print("Path -->", path)
        print("Result -->", res)
        print()

        if sum(path) > self.target:
            return

        if sum(path) == self.target:
            res.append(path)
            return

        for i in range(self.idx, len(candidates)):

            if i > self.idx and candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates[i+1:], path + [candidates[i]], res)


if __name__ == "__main__":

    result = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(result.combinationSum2(candidates, target))