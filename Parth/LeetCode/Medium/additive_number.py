"""
INCOMPLETE!
"""

class Solution:

    """

    """

    def isAdditiveNumber(self, num: str) -> bool:

        res = True
        self.dfs(num, [], res)
        return res

    def dfs(self, num, path, res):

        print("Path.. ", path)
        print("NUM... ", num)
        print("RES ", res)
        print()

        if str(sum(path)) == num[:len(path)-1]:
            #res.append(path)
            path = path[1:]
            res = True

        if len(num) == 0:
            res = False
            return

        for i in range(len(num)):
            
            if res:

                self.dfs(num[i+1:], path + [int(num[i])], res)


if __name__ == "__main__":

    result = Solution()
    num = '112358'
    print(result.isAdditiveNumber(num))

        