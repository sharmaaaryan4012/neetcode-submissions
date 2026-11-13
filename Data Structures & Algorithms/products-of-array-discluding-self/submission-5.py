class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toReturn = []
        product = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1

            if zeroCount > 1:
                product = 0

            # else:
            elif (num != 0) and (zeroCount <= 1):
                product *= num


        for num in nums:
            if num == 0:
                toReturn.append(product)

            else:
                if zeroCount == 1:
                    toReturn.append(0)

                else:
                    toReturn.append(int(product/num))

        return toReturn