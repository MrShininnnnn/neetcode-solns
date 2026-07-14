class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        stack = []
        chars_dict = {}
        chars_dict['('] = ')'
        chars_dict['{'] = '}'
        chars_dict['['] = ']'

        for c in s:
            if c in chars_dict:
                stack.append(c)
            else:
                if stack and c == chars_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False
                
        return not stack
