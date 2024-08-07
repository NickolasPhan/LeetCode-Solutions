from __future__ import print_function
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    nodeCt = 0

    def __init__(self, val=1, next=None):
        self.val = val
        self.next = None
        self.head = self
        self.nodeCt += 1

    def validate(self):
        try:
            assert self.head
        except AttributeError:
            print("No head node")
            return False
        except Exception as e:
            print(e)
            return False
        return True

    def iterate(self):
        if not self.validate():
            return

        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

    def append(self, val):
        new_node = ListNode(val)
        
        if not self.validate():
            return
        
        for node in self.iterate():
            pass
        else:
            node.next = new_node
            self.nodeCt += 1

    def print(self):
        if not self.validate():
            return

        for node in self.iterate():
            print(node.val)  
   
    def deleteNode(self, position):
        if not self.validate():
            return

        if position == self.nodeCt:
            self.head = self.head.next
            return

        actualIndex = self.nodeCt - position
        count = 1 

        temp = self.head
        prev = None
        for node in range(self.nodeCt):
            prev = temp
            temp = temp.next
            
            if actualIndex == count:
                prev.next = temp.next    

            count += 1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        head.print()

        head.deleteNode(n)
        print()
        head.print()

        return head


def main():
    myList = ListNode()

    for val in range(2,6):
        myList.append(val)

    # xList.print()
    
    userInput = int(input("\nEnter index to remove from list: "))

    sol = Solution()
    sol.removeNthFromEnd(myList, userInput)


if __name__ == "__main__":
    print()
    main()
    print()
