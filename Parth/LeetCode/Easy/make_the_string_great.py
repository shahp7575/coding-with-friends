"""
Runtime: 40 ms
Memory: 13.8 MB
"""

class Solution:

    """
    Problem Statement:
    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

    1) 0 <= i <= s.length - 2
    2) s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
    """

    def makeGood(self, s: str) -> str:

        new_str = []
        
        for i in s:
            if not new_str:
                new_str.append(i)
            elif new_str[-1].isupper() and new_str[-1].lower() == i:
                new_str.pop()
            elif new_str[-1].islower() and new_str[-1].upper() == i:
                new_str.pop()
            else:
                new_str.append(i)

        return "".join(new_str)

if __name__ == "__main__":

    result = Solution()
    string = 'AbBbbcCacdef'
    print(result.makeGood(string))
        