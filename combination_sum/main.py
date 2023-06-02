from typing import List

from itertools import chain

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dp(n, arr=[], memo={}):
            
            if n==0:
                return arr
            if n < 0:
                return None
            
            branches = []
            for num in candidates:
                b = dp(n-num, arr+[num], memo)
                if b and b not in branches:
                    # print(b)
                    branches.append(b)
            
            branches = list(chain.from_iterable(lst if isinstance(lst[0], list) else [lst] for lst in branches))
            
            return branches
        
        return dp(target)


if __name__ == "__main__":
    # print(Solution().combinationSum(candidates=[2,3,6,7], target=7))
    print(Solution().combinationSum(candidates=[2,3,5], target=8))