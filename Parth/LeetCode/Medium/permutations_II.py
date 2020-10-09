"""
Using DFS Backtracking.
Runtime: 56 ms
Memory: 14.1 MB
"""

from typing import List

class Solution:

    """
    Problem Statement: 
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):

        if not nums:
            res.append(path)
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                #print(nums[:i], "\t", nums[i+1:], "\tPath ->", nums[i], "\tRes -->", res)
                self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
        

if __name__ == "__main__":

    result = Solution()
    nums = [3, 0, 3, 3]
    print(result.permuteUnique(nums))