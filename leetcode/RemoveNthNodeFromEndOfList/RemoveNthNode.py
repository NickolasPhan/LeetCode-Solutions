from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=1, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        headCopy = head
        count = 0

        while head:
            count += 1
            # print(head.val)
            head = head.next


        actualIndex = count - n

        if actualIndex == count:
            head

        head = headCopy

        count = 0

        temp = head
        prev = None
        while head:
            
            count += 1
            if count == actualIndex:


def main():
    myList = ListNode()
    myListPtr = myList

    for val in range(2, 6):
        myListPtr.next = ListNode(val)
        myListPtr = myListPtr.next

    userIn = int(input("Enter nth number to remove from end:"))

    solution = Solution()
    solution.removeNthFromEnd(myList, userIn)

if __name__ == "__main__":
    main()
