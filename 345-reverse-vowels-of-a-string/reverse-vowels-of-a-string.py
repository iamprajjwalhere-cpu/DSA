class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set("aeiouAEIOU")       
        p,q = 0,len(s) - 1
        while p < q:
            if s[p] not in vowels:
                p += 1
            elif s[q] not in vowels:
                q -= 1
            else:
                s[p], s[q] = s[q], s[p]
                p += 1
                q -= 1
        return "".join(s)