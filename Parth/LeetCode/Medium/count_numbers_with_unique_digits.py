class Solution:

    """

    """

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        count = 0
        res = []
        self.dfs([0,1,2,3,4,5,6,7,8,9], [], res)
        return res

    def dfs(self, n, path, res):

        print(n)
        print(path)
        print(res)
        print()

        for i in range(10):

            if n[i] != n[i+1] and n[0] != 0:
                res.append(path)
            
            self.dfs(n[i+1:], [n[i]] + [n[i+1]], res)

        return n


if __name__ == "__main__":

    result = Solution()
    n = 2
    print(result.countNumbersWithUniqueDigits(n))
        