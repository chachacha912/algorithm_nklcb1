class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if self.head == None:
            return True
        return False

    def prepend(self, value):
        if self.head == None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node

    def append(self, value):
        if self.head == None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node

    def set_head(self, index):
        if self.head == None:
            return False
        
        node = self.head
        for i in range(index):
            if node.next == None:
                return False
            node = node.next
        
        self.head = node
        self.head.prev = None
        return True

    def access(self, index):
        if self.head == None:
            return None
        
        node = self.head
        for i in range(index):
            if node.next == None:
                return None
            node = node.next
        
        if node == None:
            return None
        else:
            return node.value

    def insert(self, index, value):
        if self.head == None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True
        
        node = self.head
        for i in range(index):
            if node.next == None:
                return False
            node = node.next
        
        if node == None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(value, node, node.prev)
            node.prev.next = node
        return True

    def remove(self, index):
        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return True
        
        node = self.head
        for i in range(index):
            if node.next == None:
                return False
            node = node.next
        
        if node == None:
            return False
        else:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            return True

    def print(self):
        if self.head == None:
            print('[]')
            return

        node = self.head
        while node.next:
            print(node.value, end=' ')
            node = node.next
        print(node.value)

    def print_reverse(self):
        if self.head == None:
            print('[]')
            return

        node = self.tail
        while node.prev:
            print(node.value, end=' ')
            node = node.prev
        print(node.value)


dll = DoublyLinkedList()
print('\n0. print')
dll.print()

print('\n1. is_empty')
print(dll.is_empty())

print('\n2. prepend')
dll.prepend(1)
dll.prepend(2)
dll.print()

print('\n3. append')
for i in range(5):
    dll.append(i+3)
dll.print()

print('\n4. print_reverse')
dll.print_reverse()

print('\n5. set_head')
print(dll.set_head(3))
dll.print()
print(dll.set_head(11))
dll.print()

print('\n6. access')
print(dll.access(0))
print(dll.access(5))

print('\n7. insert')
print(dll.insert(0,1))
dll.print()

print('\n8. remove')
print(dll.remove(0))
dll.print()
