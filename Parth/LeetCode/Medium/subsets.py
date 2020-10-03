from typing import List

class Solution:



    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        res.append(path)
        print("NUMS --> ", nums)
        print("PATH --> ", path)
        print("RES --> ", res)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], path + [nums[i]], res)

if __name__ == "__main__":

    result = Solution()
    nums = [1,2,3]
    print(result.subsets(nums))