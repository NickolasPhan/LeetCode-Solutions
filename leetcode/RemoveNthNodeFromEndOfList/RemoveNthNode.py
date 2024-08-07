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

        print("actualIndex:", actualIndex)
        print("count:", count)

        if actualIndex+1 == count:
            return head

        head = headCopy

        count = 0

        prev = None
        while head.next:
            prev = head
            head = head.next

            print("actualIndex:", actualIndex)
            print("count:", count)

            if count == actualIndex:
                prev.next = head.next

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
