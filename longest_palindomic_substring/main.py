class Solution:
    def longestPalindrome(self, s: str) -> int:
        return self.solve(s, start=0, end=len(s)-1)

    def solve(self, s, start, end, cache={}):
        
        if s in cache:
            return cache[s]
        
        if start >= end:
            cache[s] = -1
            return -1
        
        if len(s) == 0:
            return -1

        if len(s) == 1:
            # Always true: 'a' is a palindrome of itself.
            return 1

        # Technically an O(n) operation.
        if s == s[::-1]:
            cache[s] = len(s)
            return len(s)

        # How many choices?
        # 1: Increment start, decrement end
        # 2: Increment start, don't decrement end
        # 3. Don't increment start, don't decrement end

        b1 = self.solve(s[start+1:end], start+1, end, cache)
        b2 = self.solve(s[start:end-1], start, end-1, cache)
        b3 = self.solve(s[start+1:end-1], start+1, end-1, cache)

        cache[s] = max(b1, b2, b3)
        return cache[s]
    

if __name__ == "__main__":
    print(Solution().longestPalindrome('abccccdd'))
    print(Solution().longestPalindrome('cbbd'))
    print(Solution().longestPalindrome('bbbab'))