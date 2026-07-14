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
                if stack:
                    if c == chars_dict[stack[-1]]:
                        stack.pop()
                        continue
                return False
                
        return len(stack) == 0
