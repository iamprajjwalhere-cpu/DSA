class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_dict = {k: v for k, v in knowledge}
        
        result = []
        current_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                key = "".join(current_key)
                result.append(knowledge_dict.get(key, "?"))
                
                current_key = [] 
                in_bracket = False
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)