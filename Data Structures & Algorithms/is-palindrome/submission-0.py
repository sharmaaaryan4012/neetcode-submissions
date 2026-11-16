class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        toCheck = ""

        for char in string:
            if char.isalnum():
                toCheck += char

        if toCheck == toCheck[::-1]:
            return True

        return False