class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
    

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def put(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.tail, None)
            self.tail.next = node
            self.tail = node

    def get(self):
        if self.head is None and self.tail is None:
            return None # Underflow

        value = self.head.value
        if (self.head.next is not None):
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        return value

    def peek(self):
        if self.head is None and self.tail is None:
            return None # Underflow
        else:
            return self.head.value

    def print(self):
        if self.head is None and self.tail is None:
            print('[]')
        else:
            current = self.head
            while current.next:
                print(current.value, end=' ')
                current = current.next
            print(current.value)


linkedQ = LinkedQueue()
linkedQ.print()

linkedQ.put(1)
linkedQ.print()

for i in range(2,5):
    linkedQ.put(i)
linkedQ.print()

print(linkedQ.peek())

for i in range(6):
    print(linkedQ.get(), end=' ')
print()
linkedQ.print()

linkedQ.put(10)
print(linkedQ.peek())
linkedQ.print()