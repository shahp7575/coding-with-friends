"""
Problem Statement: The Minion Game!
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""

def minion_game(s):

    VOWEL = ['A', 'E', 'I', 'O', 'U']
    stuart = 0
    kevin = 0

    for i in range(len(s)):
        print(s[i])
        if s[i] in VOWEL:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == "__main__":

    s = 'BAANANAS'
    minion_game(s)