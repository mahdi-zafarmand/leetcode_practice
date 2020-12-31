class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        
        i = 1
        while i < len(strs) and len(prefix) > 0:
            if strs[i] == "":
                return ""
            if strs[i][0] != prefix[0]:
                return ""
            
            full_word = True
            process_len = min(len(prefix), len(strs[i]))
            for j in range(process_len):
                if prefix[j] != strs[i][j]:
                    full_word = False
                    prefix = prefix[:j]
                    break
                    
            if j == len(strs[i]) - 1 and full_word:
                prefix = strs[i]
                
            i += 1
        return prefix
    
    
#     nice Idea:
    # if not S: return ''
    # m, M, i = min(S), max(S), 0
    # for i in range(min(len(m),len(M))):
    #     if m[i] != M[i]: break
    # else: i += 1
    # return m[:i]