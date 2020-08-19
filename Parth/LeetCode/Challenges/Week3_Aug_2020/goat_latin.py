class Solution:

    """
    Problem Statement:
    A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
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
        