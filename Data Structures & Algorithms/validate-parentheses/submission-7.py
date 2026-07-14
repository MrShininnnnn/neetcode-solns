class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        q = []
        chars_dict = {}
        chars_dict['('] = ')'
        chars_dict['{'] = '}'
        chars_dict['['] = ']'

        for c in s:
            if c in chars_dict:
                q.append(c)
            else:
                if q:
                    if c == chars_dict[q[-1]]:
                        q.pop()
                        continue
                return False
                
        return not bool(q)
