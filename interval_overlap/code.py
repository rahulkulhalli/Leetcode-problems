class Solution:
    def __init__(self):
        pass
    
    @staticmethod
    def solve(array):
        
        # Sort the array first.
        sorted_arr = sorted(array, key=lambda x: x[0], reverse=False)
        
        buffer = list()
        buffer.append(sorted_arr[0])
        
        ix = 1
        while ix < len(sorted_arr):
            curr = sorted_arr[ix]
            if curr[0] <= buffer[-1][1]:
                buffer[-1][1] = curr[1]
            else:
                buffer.append(curr)
            ix += 1
        
        return buffer


if __name__ == "__main__":
    ans = Solution.solve([[7, 12], [13, 15], [1, 4], [4, 9]])
    print(ans)