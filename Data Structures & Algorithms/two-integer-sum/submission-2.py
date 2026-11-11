class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toReturn = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    toReturn.append(i)
                    toReturn.append(j)
                    return toReturn

        return toReturn