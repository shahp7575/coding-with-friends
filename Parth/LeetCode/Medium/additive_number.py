"""
INCOMPLETE!
"""

class Solution:

    """

    """

    def isAdditiveNumber(self, num: str) -> bool:

        res = []
        self.dfs(num, [], res)
        return len(res) > 0

    def dfs(self, num, path, res):

        print("Path.. ", path)
        print("NUM... ", num)
        print("RES ", res)
        print()


        for i in range(len(num)):
            
            if num[0] == '0' and i > 0:
                break
            
            if len(path) > 1 and str(sum(path)) != num[:len(str(sum(path)))]:
                continue

            if len(path) > 1 and str(sum(path)) == num[:len(str(sum(path)))]:
                res.append(path)
                path = path[1:]
                num = num[len(path)+1:]

            if num == '':
                return True

            self.dfs(num[i+1:], path + [int(num[:i+1])], res)
            


if __name__ == "__main__":

    result = Solution()
    num = '12312413'
    print(result.isAdditiveNumber(num))

        