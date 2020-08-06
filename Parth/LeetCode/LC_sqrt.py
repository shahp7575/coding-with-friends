class Solution:

    """
    Problem Statement: Compute and return the square root of x, 
    where x is guaranteed to be a non-negative integer.
    """

    def mySqrt(self, x: int) -> int:

        for i in range(1,x):
            if i*i == x:
                return i

if __name__ == "__main__":
    result = Solution()
    print(result.mySqrt(x=5))