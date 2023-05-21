class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        numset = set(nums)
        maxlen = 0
        for num in nums:
            if (num - 1) not in numset:
                curr = num
                seqlen = 0
                while (curr + 1) in numset:
                    seqlen += 1
                    curr += 1
                maxlen = max(maxlen, seqlen)
        
        return maxlen
    

if __name__ == "__main__":
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))