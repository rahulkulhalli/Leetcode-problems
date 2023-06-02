class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def dp(l, r, mystr):
            
            if len(mystr) == 0:
                return ""
            if l > r:
                return ""
            if l < 0 or r > len(mystr):
                return ""
            if l == r:
                if len(t) == 1 and mystr[0] == t:
                    return mystr[0]
                    
                return ""
            
            substr = mystr[l:r]
            
            curr_window = None
            if all([_t in substr for _t in t]):
                curr_window = substr
            
            # three choices
            b1 = dp(l+1, r, substr)
            b2 = dp(l, r-1, substr)
            b3 = dp(l+1, r-1, substr)

            minlen = int(10e5 + 1)
            minstr = None
            for b in [curr_window, b1, b2, b3]:
                if b and len(b) < minlen:
                    minlen = len(b)
                    minstr = b
            
            return minstr
        
        
        if len(t) > len(s):
            return ""
        
        if t == s:
            return s
        
        if len(t) == len(s) and t != s:
            return ""
        
        return dp(l=0, r=len(s), mystr=s)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))
    # print(sol.minWindow(s="a", t="a"))
    print(sol.minWindow(s="a", t="aa"))
    