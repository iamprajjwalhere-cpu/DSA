class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = set("aeiouAEIOU")       
        p = 0
        q = len(chars) - 1        
        while p < q:
            if chars[p] not in vowels:
                p += 1
            elif chars[q] not in vowels:
                q -= 1
            else:
                chars[p], chars[q] = chars[q], chars[p]
                p += 1
                q -= 1
        return "".join(chars)