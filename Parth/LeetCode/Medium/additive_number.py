class Solution:

    """

    """

    def isAdditiveNumber(self, num: str) -> bool:

        res = []
        self.dfs(num, [], res)
        return res

    def dfs(self, num, path, res):
        add = sum([int(i) for i in path])
        print("Path.. ", path)
        print("NUM... ", num)
        print("ADD.. ", num[:len(path)-1])
        print("SUM.. ", add)
        print()
        if add == float(num[:len(path)-1]):
            print("IT came here")
            res.append(path)
            path = []
            return

        for i in range(len(num)):
            self.dfs(num[i+1:], path + [num[i]], res)


if __name__ == "__main__":

    result = Solution()
    num = '112358'
    print(result.isAdditiveNumber(num))

        