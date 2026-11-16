class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        # toCheck = ""
        # for char in string:
        #     if char.isalnum():
        #         toCheck += char

        string = ''.join(char for char in string if char.isalnum())

        if string == string[::-1]:
            return True

        return False