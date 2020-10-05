import time

class Solution:

    "Find the factorial of a number using recursion."

    def fact(self, n: int) -> int:

        "Factorial function. Assuming that n is a positive integer or 0."
        
        if n >= 1:
            return n * self.fact(n-1)
        else:
            return 1

if __name__ == "__main__":

    result = Solution()
    n = 5
    print(result.fact(n))