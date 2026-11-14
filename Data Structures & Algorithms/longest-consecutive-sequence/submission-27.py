class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Identify start of a sequence
        # 2. Track the length
        # 3. return longest

        numsSet = set(nums)
        longest = 0

        for num in numsSet:
            # 1. Identify start of a sequence
            if (num-1) not in numsSet:
                length = 0

                # 2. Track the length
                while (num+length) in numsSet:
                    length += 1

                longest = max(longest, length)

        return longest

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     workOn = sorted(list(set(nums)))
    #     print(workOn)
    #     longest = 0
    #     count = 0 if len(workOn) == 0 else 1

    #     for i in range(len(workOn)-1):
    #         if workOn[i]+1 == workOn[i+1]:
    #             count += 1

    #         else:
    #             count = 1

    #         longest = max(longest, count)

    #     longest = max(longest, count)

    #     return longest