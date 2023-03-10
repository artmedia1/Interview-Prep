from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = []

        curr = list1
        while curr:
            merged_list.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            merged_list.append(curr.val)
            curr = curr.next

        heapq.heapify(merged_list)
        
        curr = dummy = ListNode()

        while merged_list:
            curr.next = ListNode(heapq.heappop(merged_list))
            curr = curr.next

        return dummy.next

if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    test = solution.mergeTwoLists(list1, list2)
    
    printList = []
    while test:
        printList.append(test.val)
        test = test.next
    print(printList)

            