class Solution:
    def __init__(self):
        pass
    
    
    @staticmethod
    def __recursiveSolve(array, k, n, buffer):
        
        # Array length is the depth limiter.
        if len(array) == 0:
            if len(buffer) == k:
                if sum(buffer) == n:
                    return buffer
                else:
                    return None
            else:
                return None
        
        # Two choices at every step: take or don't take.
        b1 = Solution.__recursiveSolve(array[1:], k, n, buffer+[array[0]])
        b2 = Solution.__recursiveSolve(array[1:], k, n, buffer)
        
        upper_return = []
        
        if b1 and len(b1) > 0:
            upper_return.append(b1)
        
        if b2 and len(b2) > 0:
            upper_return.append(b2)
        
        if len(upper_return) == 0:
            return None
        
        if len(upper_return) == 1:
            return upper_return[0]

        return upper_return
        
    @staticmethod
    def solve(array, k, n):
        # Given an array of integers, determine whether the sum of the combination of any k elements of the array is equal to N.
        
        res = Solution.__recursiveSolve(array, k, n, buffer=[])
        print(res)


if __name__ == "__main__":
    Solution.solve(array=[7, 10, 12, 4, 6, 21, 8, 2, 12, 13, 9, 17, 6, 7, 3], k=5, n=52)