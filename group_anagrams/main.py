class Solution:
    def groupAnagrams(self, strs):
        anagram_set = dict()
        for inp in strs:
            key = "".join(sorted(inp))
            if key not in anagram_set:
                anagram_set[key] = [inp]
            else:
                anagram_set[key].append(inp)
                
        return [v for v in anagram_set.values()]        


# Driver code.
if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # >> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]