class Solution:
    def isValid(self, s: str) -> bool:
        x = []
        for element in s:
            if element == '(' or element == '{' or element == '[':
                x.append(element)
            elif ((x == []) is False):
                if element == ')' and x[-1] == '(':
                    x.pop()
                elif element == '}' and x[-1] == '{':
                    x.pop()
                elif element == ']' and x[-1] == '[':
                    x.pop()
                else:
                    return False
            else:
                return False
        if len(x) == 0:
            return True
        return False
        