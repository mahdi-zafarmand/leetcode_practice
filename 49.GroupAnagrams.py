class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in d:
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]
                
        return [d[x] for x in d]
        
    
        # d = {}
#         for word in strs:
#             code = self.code(word)
#             if code in d:
#                 d[code].append(word)
#             else:
#                 d[code] = [word]

#         return [d[x] for x in d]

            
#     def code(self, word):
#         code_list = [0] * 26
#         for letter in word:
#             code_list[ord(letter) - ord('a')] += 1

#         return tuple(code_list)