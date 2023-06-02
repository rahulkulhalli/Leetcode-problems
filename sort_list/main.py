from typing import Optional

'''
LC #148

TODO: Implement this as merge sort.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    
    def length(self, head):
        ln = 0
        runner = head
        while runner:
            ln += 1
            runner = runner.next
        
        return ln
    
    def print_ll(self, head):
        vals = []
        runner = head
        while runner:
            vals.append(runner.val)
            runner = runner.next
        return vals
    
    def getListFromIx(self, head, ix):
        target_ix = 0
        runner = head
        while runner:
            if target_ix == ix:
                return runner
            target_ix += 1
            runner = runner.next
        
        return None
    
    def getListTillIx(self, head, ix):
        list_head = head
        runner = head
        target_ix = 0
        
        while runner:
            if target_ix == ix:
                runner.next = None
                return list_head
            target_ix += 1
            runner = runner.next
        
        return None
    
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     start = 0
    #     end = self.length(head)
        
    #     mid = (start + end)//2

def pop():
    head = ListNode(0)
    runner = head
    nums = [2,3,4,5,6]
    for num in nums:
        node = ListNode(num)
        runner.next = node
        runner = node
    return head


if __name__ == "__main__":
    ll = pop()
    sol = Solution()
    
    print(sol.print_ll(ll))
    
    ll2 = sol.getListTillIx(ll, 3)
    print(sol.print_ll(ll2))