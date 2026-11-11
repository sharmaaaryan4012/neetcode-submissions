class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sCharCount = {}
        tCharCount = {}

        for sChar, tChar in zip(s, t):
            if sChar not in sCharCount:
                sCharCount[sChar] = 1

            else:
                sCharCount[sChar] += 1

            if tChar not in tCharCount:
                tCharCount[tChar] = 1

            else:
                tCharCount[tChar] += 1


        return sCharCount == tCharCount
            

        