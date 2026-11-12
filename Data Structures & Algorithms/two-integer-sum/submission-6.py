# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         toReturn = []

#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if (nums[i] + nums[j] == target):
#                     toReturn.append(i)
#                     toReturn.append(j)
#                     return toReturn

#         return toReturn

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        toReturn = []

        for idx, ele in enumerate(nums):
            complement = target - ele

            if complement not in seen:
                seen[ele] = idx

            else:
                toReturn.append(seen[complement])
                toReturn.append(idx)

        return toReturn
