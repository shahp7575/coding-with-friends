"""
Runtime: 44 ms
Memory: 14.3 MB
"""

from typing import List

class Solution:

    """
    Problem #78 Subsets
    Given a set of distinct integers, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):

        if path not in res:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)

if __name__ == "__main__":

    result = Solution()
    nums = [1,2,3]
    print(result.subsets(nums))