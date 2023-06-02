from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amt, coins_bf, cache={}):
            
            # if amt in cache:
            #     return cache[amt]
            
            if amt == 0:
                return len(coins_bf)
            
            if amt < 0:
                # cache[amt] = None
                # return cache[amt]
                return None
            
            choices = []
            for _, coin in enumerate(coins):
                branch = dp(amt-coin, coins_bf+[coin], cache)
                if branch:
                    choices.append(branch)
            
            return_amt = min(choices) if len(choices) > 0 else -1
            
            # if amt in cache:
            #     cache[amt] = min(cache[amt], return_amt)
            # else:
            #     cache[amt] = return_amt
            

            # return cache[amt]
            return return_amt
        
        return dp(amount, coins_bf=[], cache={})
        

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange(coins = [1,2,5], amount = 11))
    print(s.coinChange(coins = [2], amount = 3))
    print(s.coinChange(coins = [2], amount = 1))