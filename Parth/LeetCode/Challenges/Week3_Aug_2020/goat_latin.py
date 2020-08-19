class Solution:

    """
    Problem Statement:

    """

    def toGoatLatin(self, S: str) -> str:

        VOWELS = 'aeiou'
        result = []

        for idx, word in enumerate(S.split()):

            if word[0].lower() in VOWELS:
                result.append(word + 'ma' + 'a'*(idx+1))
            
            if word[0].lower() not in VOWELS:
                result.append(word[1:] + word[0] + 'ma' + 'a'*(idx+1))
            

        return " ".join(result)

if __name__ == "__main__":

    result = Solution()
    string = "The quick brown fox jumped over the lazy dog"
    print(result.toGoatLatin(string))
        