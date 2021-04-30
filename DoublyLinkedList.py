"""
A doubly linked list implementation.

@author Kai Wang
"""

class DoublyLinkedList:
    """Data Structure: Doubly Linked List"""
    class Node:
        """Define Node used in Linked List"""
        def __init__(self, value, prev = None, next = None):
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, value = None):
        """
        Constructor of DoublyLinkedList
        DoublyLinkedList will be None if value = None
        """
        self.head = self.Node(value) if value else None
        self.tail = self.head
        self.size = 1 if value else 0

    def size(self):
        """Return the size of DoublyLinkedList"""
        return self.size

    def isEmpty(self):
        """Check if DoublyLinkedList is empty"""
        return self.size == 0

    def clear(self):
        """Clear all nodes in SinglyLinkedList"""
        while self.head:
            next = self.head.next
            self.head.prev = self.head.next = None
            self.head = next

        self.head = self.tail = None
        self.size = 0
    
    def addLast(self, value):
        """Add a new node with the value to the end of DoublyLinkedList"""
        if not self.isEmpty():
            self.tail.next = self.Node(value, self.tail)
            self.tail = self.tail.next
        else:
            self.head = self.Node(value)
            self.tail = self.head
        
        self.size += 1
    
    def addFirst(self, value):
        """Add a new node with the value to the very beginning of DoublyLinkedList"""
        if not self.isEmpty():
            self.head.prev = self.Node(value, None, self.head)
            self.head = self.head.prev 
        else:
            self.head = self.Node(value)
            self.tail = self.head
        
        self.size += 1

    def popFirst(self):
        """Remove the first node. Do nothing if the list is empty"""
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.size > 1:
            self.head = self.head.next
            self.size -= 1
    
    def popLast(self):
        """Remove the last node. Do nothing if the list is empty"""
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.size > 1:
            self.tail = self.tail.prev
            self.size -= 1

    def peekFirst(self):
        """Return the value of first node or last node (when reversed = True)"""
        return self.head.value if not self.isEmpty() else None
    
    def peekLast(self):
        """Return the value of last node or last node (when reversed = True)"""
        return self.tail.value if not self.isEmpty() else None
    
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
        
        trav = self.Node(0, None, self.head)
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
    dll = DoublyLinkedList()
    dll.addFirst(2)
    print(dll.toString())
    dll.addFirst(3)
    print(dll.toString())
    dll.addLast(5)
    dll.addLast(9)
    dll.addLast(8)
    print(dll.toArray())
    dll.removeAt(3)
    print(dll.toString())
    dll.peekFirst()
    dll.peekLast()
    dll.popFirst()
    print(dll.toString())
    print(dll.peekFirst())
    print(dll.peekLast())
    dll.replace(1, 6)
    print(dll.toString())
    dll.clear()
    print(dll.toString())