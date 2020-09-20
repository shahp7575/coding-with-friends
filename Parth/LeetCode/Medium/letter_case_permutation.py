import itertools
from typing import List

"""
Runtime: 48 ms
Memory: 14.2 MB
"""

class Solution:

    """
    Given a string S, we can transform every letter individually 
    to be lowercase or uppercase to create another string.
    Return a list of all possible strings we could create. 
    You can return the output in any order.
    """

    def letterCasePermutation(self, S: str) -> List[str]:
        
        L = [set([i.lower(), i.upper()]) for i in S]
        
        return list(map(''.join, itertools.product(*L)))

if __name__ == "__main__":

    result = Solution()
    s = "a1b2"
    print(result.letterCasePermutation(s))