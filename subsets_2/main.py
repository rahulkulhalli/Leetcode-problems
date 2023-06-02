from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]):
        
        heap_list = [[]]
        
        def dp(l, r):
            if l > r:
                return
            if l < 0 or r > len(nums):
                return
            
            arr = nums[l:r+1]
            
            tmp = [nums[l], nums[r]]
            if l != r:
                if tmp not in heap_list:
                    heap_list.append(tmp)
            
            if arr not in heap_list:
                heap_list.append(arr)
            
            # two choices
            dp(l+1, r)
            dp(l, r-1)
            dp(l+1, r-1)
        
        dp(l=0, r=len(nums)-1)
        
        return heap_list

if __name__ == "__main__":
    # result = Solution().subsetsWithDup([1,2,3])
    result = Solution().subsetsWithDup([1,2,2])
    print(result)
    