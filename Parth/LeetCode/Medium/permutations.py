"""
Using DFS Backtracking.
Runtime: 36 ms
Memory: 14.3 MB
"""

from typing import List

class Solution:

    """
    Problem Statement: 
    Given a collection of distinct integers, return all possible permutations.
    """

    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):

        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
        

if __name__ == "__main__":

    result = Solution()
    nums = [1,2,3]
    print(result.permute(nums))