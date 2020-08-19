"""

"""

class Solution:

    """
    Problem Statement:
    Given a non-negative integer num, repeatedly add all its digits 
    until the result has only one digit.
    """

    def addDigits(self, num: int) -> int:

        if num > 9:
            return (num - 1) % 9 + 1
        else:
            return num


if __name__ == "__main__":

    result = Solution()
    num = 9
    print(result.addDigits(num))