"""
Runtime: 44 ms
Memory: 14.3 MB
"""

from typing import List

class Solution:

    """
    Problem #90 Subsets II

    Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    Input: [1,2,2]
    Output:
    [
    [2],
    [1],
    [1,2,2],
    [2,2],
    [1,2],
    []
    ]
    """

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):

        if path not in res:
            res.append(path)

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            self.dfs(nums[i+1:], path + [nums[i]], res)

        return nums
        

if __name__ == "__main__":

    result = Solution()
    nums = [1,2,2]
    print(result.subsetsWithDup(nums))