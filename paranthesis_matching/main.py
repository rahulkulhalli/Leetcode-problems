class Solution:
    def __init__(self):
        pass
    
    def paranthesisMatching(self, expression, counter):
        if len(expression) == 0:
            if counter == 0:
                return True
            return False
        
        symbol = expression[0]
        
        res = None
        if symbol in ['[', '{', '(']:
            res = self.paranthesisMatching(expression[1:], counter+1)
        elif symbol in [']', '}', ')']:
            res = self.paranthesisMatching(expression[1:], counter-1)
        else:
            res = self.paranthesisMatching(expression[1:], counter)
        
        return res
    
    def paranthesisMatchingStack(self, expression, stack):
        if len(expression) == 0:
            if len(stack) == 0:
                return True
            return False
        
        symbol = expression[0]
        
        if symbol in ['[', '{', '(']:
            res = self.paranthesisMatchingStack(expression[1:], stack+[symbol])
        elif (symbol == ']' and stack[-1] == ']') or (symbol == '}' and stack[-1] == '}') or (symbol == ')' and stack[-1] == ')'):
            _ = stack.pop(0)
            res = self.paranthesisMatchingStack(expression[1:], stack)
        else:
            res = self.paranthesisMatchingStack(expression[1:], stack)
        
        return res


if __name__ == "__main__":
    print(Solution().paranthesisMatchingStack("{2*3}+[(]4*6)", stack=[]))
    print(Solution().paranthesisMatchingStack("{2*3}+[(2+4)+((6-4)*(8/12))]", stack=[]))