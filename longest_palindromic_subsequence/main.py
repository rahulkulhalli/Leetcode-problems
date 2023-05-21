class Solution:
    def __init__(self):
        pass
    
    def lps(self, s, buffer):
        if len(s) == 0:
            if buffer == buffer[::-1]:
                return buffer
            return None
        
        # Two choices for the subsequence: either take or don't take.
        # Let's start from the beginning index.
        b1 = self.lps(s[1:], buffer+[s[0]])
        b2 = self.lps(s[1:], buffer)
        
        accrued = []
        if b1 is not None and len(b1) > 0:
            accrued.append(b1)
        if b2 is not None and len(b2) > 0:
            accrued.append(b2)
        
        if len(accrued) == 1:
            return accrued[0]
        if len(accrued) == 2:
            # Determine the one with the max length.
            if len(accrued[0]) > len(accrued[1]):
                return accrued[0]
            return accrued[1]
        
        return None
        
    
    def longestPalindromicSubsequence(self, s):
        # set-up base recursion variables here.
        return "".join(self.lps(s, buffer=[]))
    

if __name__ == "__main__":
    print(Solution().longestPalindromicSubsequence('bbbab'))
    print(Solution().longestPalindromicSubsequence('cbbd'))