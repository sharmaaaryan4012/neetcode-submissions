class Solution:

    def encode(self, strs: List[str]) -> str:
        toReturn = ""

        for string in strs:
            toReturn += string[::-1] + 'xyz'

        return toReturn

    def decode(self, s: str) -> List[str]:
        toReturn = []

        for rev_string in s.split('xyz'):
            toReturn.append(rev_string[::-1])

        toReturn.pop()

        return toReturn