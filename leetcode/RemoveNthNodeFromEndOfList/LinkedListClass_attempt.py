from typing import Optional

# Definition for singly-linked list.
class Node:
    def __init__(self, val=1):
        self.val = val
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None 

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

    def getLength(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        
        return size

    def deleteNode(self, head, position):
        temp = self.head
        prev = None

        if temp is None:
            return self.head

        if position == 1:
            self.head = temp.next
            return self.head

        for i in range(position):
            prev = temp
            temp = temp.next
            if temp is None:
                print("Data not found")
                return head

        if temp is not None:
            prev.next = temp.next

        return head

class Solution:
    def removeNthFromEnd(self, head: Optional[Node], n: int) -> Optional[Node]:
        count = head.getLength()
        finalN = count - n 

        head.deleteNode(head.head, finalN)
        head.print()
        

def main():
    myList = LinkedList()
    myList.head = Node()

    for val in range(2, 6):
        myList.append(val)

    # xList.print()
    
    userInput = int(input("\nEnter index to remove from list: "))

    sol = Solution()
    sol.removeNthFromEnd(myList, userInput)


if __name__ == "__main__":
    print()
    main()
    print()
