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
            head = head.next

        actualIndex = count - n
        actualIndex -= 1

        head = headCopy

        if actualIndex == -1:
            head = head.next
            return head

        count = 0 

        temp = head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next

            if count == actualIndex:
                prev.next = temp.next

            count += 1

        return headCopy 

def main():
    myList = ListNode()
    myListPtr = myList

    for val in range(2, 3):
        myListPtr.next = ListNode(val)
        myListPtr = myListPtr.next

    myListPtr = myList

    while myListPtr:
        print(myListPtr.val, end=" ")
        myListPtr = myListPtr.next
    else:
        print()

    userIn = int(input("\nEnter nth number to remove from end: "))

    solution = Solution()
    head = solution.removeNthFromEnd(myList, userIn)

    print()
    while head:
        print(head.val, end=" ")
        head = head.next
    else:
        print()

if __name__ == "__main__":
    print()
    main()
    print()
