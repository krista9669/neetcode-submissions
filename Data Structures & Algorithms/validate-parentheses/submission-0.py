class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True
        else:
            pairs = {
                '(':')',
                '{':'}',
                '[':']'
            }
            for _ in s:
                if _ == '(' or _ == '{' or _ == '[':
                    stack.append(_)
                else:
                    if not stack:
                        return False
                    popped = stack.pop()
                    if pairs[popped] != _:
                        return False
        if stack:
            return False
        return True