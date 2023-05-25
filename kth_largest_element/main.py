from typing import List

# TODO: INCOMPLETE

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(nums)
        maxnum = -1

        for n in nums:
            if n > maxnum:
                maxnum = n
        
        sorter = dict()

        index = len(nums)
        sorter = dict()
        sorter[index] = maxnum

        for ix, num in enumerate(nums):
            if num < maxnum:
                maxnum = num
                sorter[index-1] = num
                index -= 1
        
        print(sorter)


if __name__ == "__main__":
    Solution().findKthLargest([3,2,1,5,6,4], k=2)