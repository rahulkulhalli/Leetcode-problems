from typing import List
from functools import lru_cache


class Solution:

    def maxArea(self, height: List[int]) -> int:
        
        @lru_cache
        def dp(left, right):

            if left >= right:
                return 0

            # Choices?
            # Increment left by 1
            # Decrement right by 1
            # left+1, right-1

            area = (right - left) * min(height[left], height[right])

            c1 = dp(left+1, right)
            c2 = dp(left, right-1)
            c3 = dp(left+1, right-1)

            return max(area, c1, c2, c3)

        return dp(left=0, right=len(height)-1)
    
if __name__ == "__main__":
    print(Solution().maxArea([2,3,4,5,18,17,6]))
    print(Solution().maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,
                              111,128,50,58,2,112,179,2,100,111,115,76,134,120,
                              118,103,31,146,58,198,134,38,104,170,25,92,112,
                              199,49,140,135,160,20,185,171,23,98,150,177,198,
                              61,92,26,147,164,144,51,196,42,109,194,177,100,99,
                              99,125,143,12,76,192,152,11,152,124,197,123,147,95,
                              73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,
                              198,126,191]))