
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        toReturn = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            num1 = nums[i]
            left = i+1
            right = len(nums)-1

            while left < right:
                num2 = nums[left]
                num3 = nums[right]

                if num2 + num3 > -num1:
                    right -= 1

                elif num2 + num3 < -num1:
                    left += 1

                else:
                    toReturn.append([num1, num2, num3])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return toReturn


        # toReturn = []
        # nums = sorted(nums)

        # print(nums)

        # for i in range(len(nums)-1):
        #     num1 = nums[i]
        #     seen = set()

        #     for j in range(i+1, len(nums)):
        #         num2 = nums[j]
        #         comp = -num1-num2

        #         if comp in seen:
        #             ele = sorted([num1, num2, comp])
        #             if ele not in toReturn:
        #                 toReturn.append(ele)

        #         seen.add(num2)

        # return toReturn



# Naive approach O(n^3):

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