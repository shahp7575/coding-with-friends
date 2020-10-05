class Solution:

    "Find the nth fibonacci number using recursion!"

    def fibb(self, n: int) -> int:

        if n >= 3:
            return self.fibb(n-1) + self.fibb(n-2)
        else:
            return 1


if __name__ == "__main__":

    result = Solution()
    n = 9
    print(result.fibb(n))