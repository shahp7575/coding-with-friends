"""
INCOMPLETE
"""

class Solution:

    """
    Problem Statement:

    """

    def makeGood(self, s: str) -> str:

        upper = [char for char in s if char.isupper()]
        print(upper)
        new_str = ""
        while len(upper) > 0:
            idx = s.find(upper[0])
            new_str = s[]
            upper.pop()
            

if __name__ == "__main__":

    result = Solution()
    string = 'leEeetcode'
    print(result.makeGood(string))
        