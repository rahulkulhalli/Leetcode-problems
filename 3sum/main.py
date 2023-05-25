from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def dp(nums, buffer=[]):
            if len(nums) == 0:
                if len(buffer) == 3:
                    if sum(buffer) == 0:
                        return buffer
                    else:
                        return []
                else:
                    return []

            results = []
            b1 = dp(nums[1:], buffer)
            b2 = dp(nums[1:], buffer+[nums[0]])

            if len(b1) > 0:
                results.append(b1)
            if len(b2) > 0:
                results.append(b2)
            
            if len(results) == 2:
                return results
            if len(results) == 1:
                return results[0]
            
            return results
        
        result = dp(nums)
        
        if len(result) == 3 and isinstance(result[0], int):
            return [result]
        
        return_arr = []
        set_arr = []
        
        for r in result:
            if len(r) == 3:
                if set(r) not in set_arr:
                    return_arr.append(r)
                    set_arr.append(set(r))
            else:
                for ir in r:
                    if set(ir) not in set_arr:
                        return_arr.append(ir)
                        set_arr.append(set(ir))
        
        return return_arr


if __name__ == "__main__":
    # print(Solution().threeSum([-1,0,1,2,-1,-4]))
    # print(Solution().threeSum([0, 1, 1]))
    # print(Solution().threeSum([0, 0, 0]))
    print(Solution().threeSum([0, 0, 0, 0]))