"""
INCOMPLETE
"""

class Solution:

    """
    Problem Statement:

    """

    def makeGood(self, s: str) -> str:

        s_list = [char for char in s]
        print(s_list)
        new_str = []
        
        for i in s_list:
            
            if i.isupper():
                s_list.remove(i)
                s_list.pop()


        return "".join(s_list)

if __name__ == "__main__":

    result = Solution()
    string = 'abBacC'
    print(result.makeGood(string))
        