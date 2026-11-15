class Solution:
    def isValid(self, s: str) -> bool:
        """
            1. convert string to list/stack
            2. pop and then match the next
            3. if popped is open (, {, [ then look for the matching bracket
            4. if open bracket is found, we keep looking to close that, in-order
        """
        lst = list(s)
        match = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        if len(lst) == 0 or (len(lst) % 2):
            return False

        for char in lst:
            if char in match.keys():
                stack.append(char)

            else:
                if len(stack) < 1 or match[stack.pop()] != char:
                    return False

        if len(stack) != 0:
            return False
            
        return True