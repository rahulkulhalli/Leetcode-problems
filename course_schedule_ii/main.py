from typing import List


class Solution:

    def getKey(self, d, val):
        for (k, v) in d.items():
            if v == val:
                return k
        return None

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses == 0:
            return []
        
        if len(prerequisites) == 0:
            return list(range(numCourses))
        
        mapper = dict()
        mapper[0] = []

        for arr in prerequisites:
            if arr[0] not in mapper:
                mapper[arr[0]] = [arr[1]]
            else:
                mapper[arr[0]].append(arr[1])
        
        keys = list(mapper.keys())
        
        vals = [mapper[k] for k in keys]

        # two-level sorting
        # 1. sort by length
        vals = list(sorted(vals, key=lambda x: len(x)))
        # 2. sort internal arrs
        vals = [list(sorted(x)) for x in vals]
        
        return_list = []
        val_ix = 0
        while len(mapper.keys()) > 0:
            k = self.getKey(mapper, vals[val_ix])
            
            # Update mapper.
            del mapper[k]
            
            return_list.append(k)
            
            val_ix += 1
        
        return return_list


if __name__ == "__main__":
    # Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    print(Solution().findOrder(2, [[1,0]]))