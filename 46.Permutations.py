class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        last_elem = nums.pop()
        x = self.permute(nums)
        y = []
        for perm in x:
            for pos in range(len(perm) + 1):
                perm.insert(pos, last_elem)
                y.append(list(perm))
                perm.pop(pos)
                
        return y