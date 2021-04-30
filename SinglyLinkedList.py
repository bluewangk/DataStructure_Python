"""
A singly linked list implementation.

@author Kai Wang
"""

class SinglyLinkedList:
    """Data Structure: Singly Linked List"""
    class Node:
        """Define Node used in Linked List"""
        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self, value = None):
        """
        Constructor of SinglyLinkedList
        SinglyLinkedList will be empty if value = None
        """
        self.head = self.Node(value) if value else None
        self.tail = self.head
        self.size = 1 if value else 0

    def size(self):
        """Return the size of SinglyLinkedList"""
        return self.size

    def isEmpty(self):
        """Check if SinglyLinkedList is empty"""
        return self.size == 0

    def clear(self):
        """Clear all nodes in SinglyLinkedList"""
        while self.head:
            next = self.head.next
            self.head.next = None
            self.head = next

        self.head = self.tail = None
        self.size = 0
    
    def add(self, value):
        """Add a new node with the value into SinglyLinkedList"""
        if not self.isEmpty():
            self.tail.next = self.Node(value)
            self.tail = self.tail.next
        else:
            self.head = self.Node(value)
            self.tail = self.head
        
        self.size += 1

    def pop(self):
        """Remove the last node. Do nothing if the list is empty"""
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.size > 1:
            trav = self.head
            while trav.next.next:
                trav = trav.next
            
            trav.next = None
            self.tail = trav
            self.size -= 1

    def peek(self, reversed = False):
        """Return the value of first node or last node (when reversed = True)"""
        if reversed:
            return self.tail.value if self.tail else None
        
        return self.head.value if self.head else None

    def indexOf(self, target):
        """Return the index of target value in the list. Return -1 if not found"""
        index = 0
        trav = self.head
        while trav:
            if trav.value == target:
                return index
            index += 1
            trav = trav.next
        
        return -1

    def removeAt(self, index):
        """Remove the node at the index. Return True if successful, otherwise retrurn False"""
        if index < 0 or index > self.size - 1:
            return False
        
        trav = self.Node(0, self.head)
        while trav and index > 0:
            index -= 1
            trav = trav.next
        
        next = trav.next
        trav.next = trav.next.next
        if next == self.head:
            self.head = trav.next
        next = None
        
        self.size -= 1

        return True

    def get(self, index):
        """Return the value at specified index"""
        if index < 0 or index > self.size - 1:
            return None
        
        trav = self.head
        while index > 0:
            index -= 1
            trav = trav.next
        
        return trav.value

    def replace(self, index, element):
        """Change the value at specified index. Return True if successful, else return False"""
        if index < 0 or index > self.size - 1:
            return False
        
        trav = self.head
        while index > 0:
            index -= 1
            trav = trav.next
        trav.value = element
        
        return True

    def contains(self, value):
        """Check if the value is contained in the list"""
        trav = self.head
        while trav.next:
            if trav.value == value:
                return True
            trav = trav.next
        return False

    def toArray(self):
        """Convert the list to array/list"""
        arr = []
        trav = self.head
        while trav:
            arr.append(trav.value)
            trav = trav.next
        
        return arr

    def toString(self):
        """Convert the list to string"""
        string = ""
        trav = self.head
        while trav:
            if not string:
                string += f'{trav.value}'
            else:
                string += "->" + f'{trav.value}'
            trav = trav.next
        
        return string

if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.add(2)
    print(sll.toString())
    sll.add(3)
    print(sll.toString())
    sll.add(5)
    sll.add(7)
    sll.add(8)
    sll.removeAt(3)
    print(sll.toArray())
    print(sll.toString())
    sll.peek()
    sll.pop()
    print(sll.toString())
    print(sll.peek())
    print(sll.peek(reversed=True))
    sll.replace(1, 6)
    print(sll.toString())
    sll.clear()
    print(sll.toString())