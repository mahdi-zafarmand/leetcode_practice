class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # intervals.sort(key=lambda x: x[0])

        intervals = self.my_sort(intervals)
        
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][1]:
                intervals[i+1][1] = intervals[i][1]
                intervals.pop(i+1)
                i -= 1
            elif intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                intervals.pop(i)
                i -= 1
            i += 1
            
        return intervals
        
    def my_sort(self, x):
        lx2 = len(x) // 2        
        return self.my_merge(self.merge(x[: lx2]), self.merge(x[lx2 :]))
    
    def my_merge(self, left, right):
        sorted_output = []
        
        i, j, ll, lr = 0, 0, len(left), len(right)
        while i < ll and j < lr:
            if left[i][0] < right[j][0]:
                sorted_output.append(left[i])
                i += 1
            else:
                sorted_output.append(right[j])
                j += 1
        
        if i < ll:
            return sorted_output + left[i:]
            
        if j < lr:
            return sorted_output + right[j:]
                    