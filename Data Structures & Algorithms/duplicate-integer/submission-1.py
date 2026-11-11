class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = {}

        for ele in nums:
            # if element not in dict, initialize the count
            
            if ele not in numCount: # if ele not in list(numCount.keys()):
            
                numCount[ele] = 1

            # else just increment
            else:
                return True
        
        return False