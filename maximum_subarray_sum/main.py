class Solution:

    def _key(self, arr):
        return "".join([str(x) for x in arr])

    def _startRecursion(self, arr, start, end, cache={}):
        
        key = self._key(arr)
        
        if key in cache:
            return cache[key]
        
        if len(arr) == 2:
            cache[key] = [max(arr[0], arr[1], sum(arr))]
            return cache[key]
        
        if len(arr) == 1:
            cache[key] = [arr[0]]
            return cache[key]
        
        if len(arr) == 0 or start > end:
            cache[key] = None
            return cache[key]

        b1 = self._startRecursion(arr[start+1:end], start+1, end)
        b2 = self._startRecursion(arr[start:end-1], start, end-1)
        b3 = self._startRecursion(arr[start+1:end-1], start+1, end-1)

        contenders = [arr]
        
        for b in [b1, b2, b3]:
            if b is not None:
                contenders.append(b)
        
        cache[key] = [max([sum(x) for x in contenders])]
        return cache[key]

    def maxSubArray(self, nums):
        max_sum = self._startRecursion(nums, start=0, end=len(nums))
        return max_sum[0]
    
    
if __name__ == "__main__":
    arr = [5,4,-1,7,8]
    arr2 = [2,0,3,-2]
    print(Solution().maxSubArray(arr2))