"""
Not working. Check later.
"""

from typing import List

class Solution:

    """
    
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        #nums.sort()
        self.len = len(nums)
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):

        print("Nums: ", nums)
        print("Path: ", path)            
        print("Res: ", res)
        print()

        if len(path) == 3 and sum(path) == 0 and sorted(path) not in res:
            res.append(sorted(path))
            path = path[1:]
        elif len(path) == 3 and sum(path) != 0:
            path = path[1:]

        for i in range(len(nums)):
            if i > 0 and len(nums) == self.len:
                break
            else:
                self.dfs(nums[i+1:], path + [nums[i]], res)

    
if __name__ == "__main__":

    result = Solution()
    #nums = [-1,0,1,2,-1,-4]
    #nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    nums = [1,-1,-1,0]
    print(result.threeSum(nums))
        