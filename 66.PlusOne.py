class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
# #         recursive implementation
#         if digits[-1] != 9:
#             new_digits = list(digits)
#             new_digits[-1] += 1
#             return new_digits
#         elif len(digits) == 1:
#             return [1, 0]
#         else:
#             new_digits = list(digits)
#             final_digits = self.plusOne(new_digits[:-1])
#             final_digits.append(0)
#             return final_digits
        
    def plusOne(self, digits: List[int]) -> List[int]:
#         iterative implemtation
        length = len(digits) - 1
        need_extra_digit = False
        while length >= 0:
            if digits[length] != 9:
                digits[length] += 1
                return digits
            if digits[length] == 9:
                digits[length] = 0
                length -= 1
        digits.insert(0, 1)
        return digits
            
                
