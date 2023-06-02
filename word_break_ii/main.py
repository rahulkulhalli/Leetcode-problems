from typing import List
from itertools import chain


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dp(mystr, words, myarr=[]):
            
            if len(mystr) == 0 or len(words) == 0:
                return myarr
            
            results = []
            
            for word in words:
                if mystr.startswith(word):
                    wordlen = len(word)
                    b1 = dp(mystr[wordlen:], words, myarr+[word])
                    if b1:
                        results.append(b1)
            
            
            results = list(chain.from_iterable(lst if isinstance(lst[0], list) else [lst] for lst in results))
            return results

        results = dp(s, wordDict)
        results = [" ".join(result) for result in results]
        return results

if __name__ == "__main__":
    print(Solution().wordBreak(s='pineapplepenapple', wordDict=["apple","pen","applepen","pine","pineapple"]))