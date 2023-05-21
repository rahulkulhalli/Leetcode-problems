class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        runnerA = headA
        runnerB = headB
        
        if runnerA is None or runnerB is None:
            return None
        
        while runnerA != runnerB:
            
            if not runnerA:
                runnerA = headB
            else:
                runnerA = runnerA.next
                
            if not runnerB:
                runnerB = headA
            else:
                runnerB = runnerB.next
        
        return runnerA


def create_ll():
    nums = [i for i in range(10)]
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        node = ListNode(num)
        current.next = node
        current = node
    
    return head
    

        
if __name__ == "__main__":
    
    l = create_ll()
    print(Solution()._compute_length(l))
    
    # Solution().getIntersectionNode()