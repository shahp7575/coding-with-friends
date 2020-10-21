"""
INCOMPLETE!
"""

class Solution:

    """

    """

    def isAdditiveNumber(self, num: str) -> bool:

        res = []
        self.dfs(num, [], res)
        return res

    def dfs(self, num, path, res):
        add = sum(path)
        print("Path.. ", path)
        print("NUM... ", num)
        print("First.. ", num[:len(path)-1])
        print("RES ", res)
        print()

        for i in range(len(num)):
            if sum(path) == int(float(num[:len(path)-1])):
                res.append(path)
                return
            self.dfs(num[i+1:], path + [int(num[i])], res)


if __name__ == "__main__":

    result = Solution()
    num = '112358'
    print(result.isAdditiveNumber(num))

        