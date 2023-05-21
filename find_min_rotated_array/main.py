class Solution:

    def binSearch(self, currmin, nums):

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] < currmin:
                return nums[0]
            return currmin

        low = 0
        high = len(nums)-1
        mid = (low + high)//2

        if nums[mid] > nums[mid+1]:
            # This means that the list begins rotation from here.
            return nums[mid+1]

        b1_arr = nums[low:mid+1] if low != mid else [nums[mid]]
        b2_arr = nums[mid+1:high+1] if high != mid else [nums[mid]]

        b1 = self.binSearch(nums[mid], b1_arr)
        b2 = self.binSearch(nums[mid], b2_arr)

        return min(b1, b2)

    def findMin(self, nums):
        maxnum = 5001
        return self.binSearch(maxnum, nums)


if __name__ == "__main__":
    print(Solution().findMin([4,5,6,7,0,1,2]))
    print(Solution().findMin([11,13,15,17]))
    print(Solution().findMin([1, 2]))
    print(Solution().findMin([2,3,4,5,1]))
    print(Solution().findMin([4,5,1,2,3]))