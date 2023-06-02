class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(num, cache={}):

            if num in cache:
                return cache[num]

            if num == 0:
                cache[num] = 1
                return cache[num]
            if num < 0:
                cache[num] = 0
                return cache[num]
            
            # two choices - either 1 or 2 steps
            b1 = dp(num-1, cache)
            b2 = dp(num-2, cache)

            cache[num] = b1 + b2
            return cache[num]
        
        return dp(n)


if __name__ == "__main__":
    # print(Solution().climbStairs(2))
    # print(Solution().climbStairs(3))
    print(Solution().climbStairs(5))