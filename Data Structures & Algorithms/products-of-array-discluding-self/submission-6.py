class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toReturn = []
        product = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num

        for num in nums:
            if zeroCount >= 2:
                toReturn.append(0)

            elif zeroCount == 1:
                if num == 0:
                    toReturn.append(product)
                else:
                    toReturn.append(0)

            else:
                toReturn.append(product // num)

        return toReturn