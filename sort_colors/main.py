from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(len(nums)):
            ix = 1
            while ix < len(nums):
                if nums[ix] < nums[ix-1]:
                    # Swap the numbers
                    swap1, swap2 = nums[ix], nums[ix-1]
                    nums[ix] = swap2
                    nums[ix-1] = swap1

                ix += 1



if __name__ == "__main__":
    arr = [2,0,2,1,1,0]
    print("original: ", arr)
    Solution().sortColors(arr)