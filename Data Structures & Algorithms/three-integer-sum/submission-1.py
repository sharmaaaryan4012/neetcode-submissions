class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            1. 3Sum -> 2Sum: (num1 + num2 + num3 == 0) -> (num2 + num3 == -num1)
        """
        toReturn = []
        nums = sorted(nums)

        print(nums)

        for i in range(len(nums)-1):
            num1 = nums[i]
            seen = set()

            for j in range(i+1, len(nums)):
                num2 = nums[j]
                comp = -num1-num2

                if comp in seen:
                    ele = sorted([num1, num2, comp])
                    if ele not in toReturn:
                        toReturn.append(ele)

                seen.add(num2)

        return toReturn

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     toReturn = []
        
    #     for i in range(len(nums)-2):
    #         num1 = nums[i]

    #         for j in range(i+1, len(nums)-1):
    #             num2 = nums[j]

    #             for k in range(j+1, len(nums)):
    #                 num3 = nums[k]

    #                 if num1+num2+num3 == 0:
    #                     toReturn.append([num1, num2, num3])

    #     return toReturn