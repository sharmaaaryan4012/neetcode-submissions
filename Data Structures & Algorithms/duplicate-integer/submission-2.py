class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numCount = {}

        # for ele in nums:
        #     if ele not in numCount:
        #         numCount[ele] = 1
        #     else:
        #         return True
        # return False

        return len(nums) != len(set(nums))