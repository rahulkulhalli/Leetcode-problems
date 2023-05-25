from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def length(self, node: ListNode) -> int:
        runner = node
        length = 0
        while runner:
            runner = runner.next
            length += 1
        return length
    
    def getIndexOf(self, node: ListNode, val: int) -> List[int]:
        runner = node
        indices = []
        ix = 0
        while runner:
            value = runner.val
            if value == val:
                indices.append(ix)
            ix += 1
            runner = runner.next
        return indices
    
    def traverseTillIndex(self, node: ListNode, ix: int) -> ListNode:
        runner = node
        curr_ix = 0
        while runner:
            if curr_ix == ix:
                return runner
            runner = runner.next
            curr_ix += 1
        return None
    
    def moveNodeToIndex(self, node: ListNode, ix: int) -> ListNode:
        pass
        
    
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # just swap
        runnerA = head


def populate():
    nums = [7, 4, 3, 2, 0, 1, 5]
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        node = ListNode(num)
        curr.next = node
        curr = node
        
    return head


def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    
    print(vals)


def swap(head, val1, val2):
    
    sol = Solution()
    
    ix1 = sol.getIndexOf(head, val1)[0]
    curr1 = sol.traverseTillIndex(head, ix1)
    prev1 = sol.traverseTillIndex(head, ix1-1)
    
    ix2 = sol.getIndexOf(head, val2)[0]
    curr2 = sol.traverseTillIndex(head, ix2)
    prev2 = sol.traverseTillIndex(head, ix2-1)
    
    if not ix1 or not ix2:
        return head
    
    if prev1:
        prev1.next = curr2
    else:
        head = curr2  
    
    if prev2:
        prev2.next = curr1
    else:
        head = curr1
    
    
    temp = curr1.next
    curr1.next = curr2.next
    curr2.next = temp
    
    return head
    

if __name__ == "__main__":
    sol = Solution()
    head = populate()
    length = sol.length(head)
    for _ in range(length):
        ix = 1
        while ix < length:
            curr = sol.traverseTillIndex(head, ix).val
            prev = sol.traverseTillIndex(head, ix-1).val
            if curr < prev:
                head = swap(head, curr, prev)
                print_list(head)
            ix += 1
    
    # print_list(head)