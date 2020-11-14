from typing import List

class Solution:

    """

    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):

        print("Nums: ", nums)
        print("Path: ", path)            
        print("Res: ", res)
        print()

        if len(path) == 3 and sum(path) == 0 and path not in res:
            res.append(path)
            path = []
        elif len(path) == 3 and sum(path) != 0:
            path = []

        for i in range(len(nums)):
            
            if sum(path) > 0:
                print("Continuing...")
                continue
            self.dfs(nums[i+1:], path + [nums[i]], res)

    
if __name__ == "__main__":

    result = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(result.threeSum(nums))
        