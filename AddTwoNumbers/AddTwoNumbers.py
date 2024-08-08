from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1head = l1
        l2head = l2

        l1Str = ""

        while l1:
            l1Str += str(l1.val)
            l1 = l1.next

        l2Str = ""

        while l2:
            l2Str += str(l2.val)
            l2 = l2.next

        l1int = int(l1Str[::-1])
        l2int = int(l2Str[::-1])

        '''
        print("\n", f"{l1int:,}", sep="")
        print(f"{l2int:,}", sep="")
        '''

        resInt = l1int + l2int

        # print("result:", f"{resInt:,}", end="\n\n")

        resStr = str(resInt)[::-1]
        resList = ListNode(int(resStr[0]))

        resListHead = resList

        for i in range(1, len(resStr)):
            resList.next = ListNode(int(resStr[i]))
            resList = resList.next

        '''
        resList = resListHead
        while resList:
            print(resList.val, end=" ")
            resList = resList.next

        print()
        '''

        return resListHead

def main():
    num = random.randint(1,9)

    myList1 = ListNode(num)
    myList1Ptr = myList1

    num = random.randint(1,9)

    myList2 = ListNode(num)
    myList2Ptr = myList2
    
    list1_len = random.randint(1,9)
    list2_len = random.randint(1,9)

    for i in range(2, list1_len+1):
    
        num = int(random.randint(1,9))

        myList1Ptr.next = ListNode(num)
        myList1Ptr = myList1Ptr.next

    for i in range(2, list2_len+1):
    
        num = int(random.randint(1,9))

        myList2Ptr.next = ListNode(num)
        myList2Ptr = myList2Ptr.next

    myList1Ptr = myList1
    myList2Ptr = myList2

    print()
    while myList1Ptr:
        print(myList1Ptr.val, end=" ")
        myList1Ptr = myList1Ptr.next
    else:
        print()

    while myList2Ptr:
        print(myList2Ptr.val, end=" ")
        myList2Ptr = myList2Ptr.next
    else:
        print()

    solution = Solution()
    solution.addTwoNumbers(myList1, myList2)

if __name__ == "__main__":
    print("====================")
    main()
    print("====================")
