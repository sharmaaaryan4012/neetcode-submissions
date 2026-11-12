class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = {}

        for num in nums:
            if num not in numCounts:
                numCounts[num] = 1

            else:
                numCounts[num] += 1

        toReturn = []

        dictPairs = numCounts.items()
        sortCounts = sorted(dictPairs, key=lambda x:x[1], reverse= True)

        for i in range(k):
            toReturn.append(sortCounts[i][0])

        

        # for _ in range(k):
        #     maxCount = -1
        #     maxK = -1

        #     for i in range(len(numCounts)):
        #         val = list(numCounts.values())[i]
        #         if maxCount < val:
        #             maxCount = val
        #             maxK = list(numCounts.keys())[i]

        #     toReturn.append(maxK)
        #     numCounts.pop(maxK)

        return toReturn