from typing import List

class Solution:

    """

    """

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        self.k = k
        self.n = n
        nl = [i for i in range(1,n)]
        self.dfs(nl, [], res)
        return res

    def dfs(self, n, path, res):

        print("N.  -> ", n)
        print("Path - >", path)
        print("RES --->", res)
        print()

        if len(path[-self.k:]) == self.k and sum(path[-self.k:]) == self.n and path[-self.k:] not in path:

            res.append(path[-self.k:])
            return

        if sum(path[-self.k:]) > self.n:
            return

        for i in range(0, len(n)):
        
            self.dfs(n[i+1:], path + [ n[i] ], res)





if __name__ == "__main__":

    result = Solution()
    k = 3
    n = 9
    print(result.combinationSum3(k ,n))