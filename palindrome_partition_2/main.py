"""
Given a string s, partition s such that every 
substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""

class Solution:
    
    def _startRecursion(self, s):
        
        if len(s) <=1 :
            return 0
        
        if s == s[::-1]:
            return True
        
        returns = []
        
        for cut_ix in range(1, len(s)-1):
            substr1 = self._startRecursion(s[:cut_ix])
            substr2 = self._startRecursion(s[cut_ix:])

            if substr1 and substr2:
                returns.append(1)
            else:
                returns.append(0)
        
        
    
    def minCut(self, s: str) -> int:
        return self._startRecursion(s)
    

if __name__ == "__main__":
    
        """
        assd
        0
        
        apa|a
        1
        
        abajx|xjaba
        1
        
        aa|bb|cc
        2
        
        aba|babababab
        1
        
        """