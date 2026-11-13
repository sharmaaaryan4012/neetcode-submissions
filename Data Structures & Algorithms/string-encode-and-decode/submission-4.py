class Solution:
    def encode(self, strs: List[str]) -> str:
        toReturn = ""
        for string in strs:
            toReturn += f"{len(string)}||{string[::-1]}"
        return toReturn

    def decode(self, s: str) -> List[str]:
        toReturn = []
        i = 0

        while i < len(s):
            j = s.find("||", i)

            length = int(s[i:j])

            start = j + 2
            end = start + length

            string = s[start:end]
            toReturn.append(string[::-1])

            i = end

        return toReturn
        
    # def encode(self, strs: List[str]) -> str:
    #     toReturn = ""

    #     for string in strs:
    #         toReturn += string[::-1] + 'xyz'

    #     return toReturn

    # def decode(self, s: str) -> List[str]:
    #     toReturn = []

    #     for rev_string in s.split('xyz'):
    #         toReturn.append(rev_string[::-1])

    #     toReturn.pop()

    #     return toReturn