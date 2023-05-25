from typing import List

class Solution:
    def findIslands(self, nums: List[List[str]]) -> int:
        
        def get_submatrix(rs, re, cs, ce):
            ncols = len(nums[0])
            nrows = len(nums)
            
            # re and ce are exclusive.
            if rs == re and cs == ce:
                return [[nums[rs][cs]]]
            if rs == re:
                rows = nums[rs]
                return [rows[cs:ce+1]] if ce+1<=ncols else None 
            if cs == ce:
                rows = nums[rs:re+1] if re+1<=nrows else None
                if rows:
                    return [[row[cs] for row in rows]]
                return None
            
            return [x[cs:ce] for x in nums[rs:re]]
        
        def is_island(x):
            if isinstance(x[0], list):
                return all([_x == "1" for _x in sum(x, [])])
            return all([_x == "1" for _x in x])
        
        def dp(rs, re, cs, ce, island_count=0):
            
            if rs < 0 or cs < 0 or re > len(nums) or ce > len(nums[0]):
                return island_count
            
            if rs > re or cs > ce:
                return island_count
            
            submatrix = get_submatrix(rs, re, cs, ce)
            
            if not submatrix:
                return island_count
            
            if is_island(submatrix):
                # print(submatrix)
                return island_count+1
            
            # multiple choices T.T
            b1 = dp(rs+1, re, cs, ce, island_count)
            b2 = dp(rs, re-1, cs, ce, island_count)
            b3 = dp(rs+1, re-1, cs, ce, island_count)
            b4 = dp(rs, re, cs+1, ce, island_count)
            b5 = dp(rs, re, cs, ce-1, island_count)
            b6 = dp(rs, re, cs+1, ce-1, island_count)
            b7 = dp(rs+1, re-1, cs+1, ce-1, island_count)
            
            print(submatrix)
            print(b1, b2, b3, b4, b5, b6, b7)
            print()
            return max(b1, b2, b3, b4, b5, b6, b7)
            
        return dp(rs=0, re=len(nums)-1, cs=0, ce=len(nums[0])-1)


if __name__ == "__main__":
    sol = Solution()
    
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    
    print(sol.findIslands(grid))