class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i)
        #         i -= 1
        #     i += 1
        # return len(nums)
        
        
        # length = 0
        # if len(nums) == 0: return length
        # for i in range(1,len(nums)):
        #     if nums[length] < nums[i]:
        #         length += 1
        #         nums[length] = nums[i]
        # return length+1
        
        x = 0
        for i in range(1, len(nums)):
            if nums[x] < nums[i]:
                x += 1
                nums[x] = nums[i]
        return x + 1
            