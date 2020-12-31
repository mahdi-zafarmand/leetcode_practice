class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            res.append(self.helper(res[-1]))
        return res
        
        
    def helper(self, L):
        x = [1]
        for i in range(len(L)-1):
            x.append(L[i] + L[i+1])
        x.append(1)
        return x