class Solution:

    def isValid(self, s: str) -> bool:
        m = []
        mapping = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in mapping:
                top_element = m.pop() if m else "#"
                if mapping[i] != top_element:
                    return False
            else:
                m.append(i)
        return not m