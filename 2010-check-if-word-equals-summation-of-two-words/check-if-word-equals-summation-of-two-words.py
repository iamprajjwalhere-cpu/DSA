class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def value(s):
            num = 0
            for i in s:
                num = num * 10 + (ord(i) - ord('a'))
            return num
        
        return value(firstWord) + value(secondWord) == value(targetWord)