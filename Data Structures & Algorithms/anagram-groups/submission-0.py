class Solution:
    def countChars(self, string: str) -> tuple[int]:
        countLst = []

        for i in range(26):
            countLst.append(0)
        
        for char in string:
            countLst[ord(char)-97] += 1

        return tuple(countLst)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        returnDict = {}

        for string in strs:
            key = self.countChars(string)
            if key not in returnDict:
                returnDict[key] = [string]
            
            else:
                returnDict[key].append(string)

        return list(returnDict.values())