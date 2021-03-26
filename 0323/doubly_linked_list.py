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
        return self.head == None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next

    def set_head(self, index):
        if self.head is None:
            return False

        prev_node = self.head
        for i in range(index):
            if prev_node is None:
                return False
            prev_node = prev_node.next 
        
        self.head = prev_node
        self.head.prev = None

        return True

    def set_tail(self, index):
        if DoublyLinkedList.is_empty(self):
            print('SSL is empty!')
        else:
            node = self.head
            idx = 0
            while node:
                if idx == index:
                    self.tail = node
                    self.tail.next = None
                    return
                node = node.next
                idx += 1
            print('Invalid index check the size of SSL')

    def access(self, index):
        if self.head is None:
            return None

        curr_node = self.head
        for i in range(index):
            if curr_node.next is None:
                print('dd2')
                return None
            curr_node = curr_node.next
            
        return curr_node.value


    def insert(self, index, value):

        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True
        else:
            curr_node = self.head
            for i in range(index):
                if curr_node.next is None:
                    if i == index-1:
                        curr_node = Node(value, None, self.tail)
                        self.tail.next = curr_node
                        self.tail = curr_node
                        return True
                    else:
                        return False
                curr_node = curr_node.next 
        new_Node = Node(value, curr_node, curr_node.prev)
        curr_node.prev.next = new_Node
        curr_node.prev= new_Node
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
            print(i)
            if node is None:
                return False
            node = node.next
        
        if node == None:
            return False
        else:
            node.prev.next = node.next
            if node.next:
                print(111)
                node.next.prev = node.prev
            else:
                print(222)
                self.tail = node.prev
            print(333)
            return True

    def print(self):
        if self.head is None:
            print('[]')
            return
        else:
            node = self.head
            while node:
                print(node.value, end = ' ')
                node = node.next
            print()

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
print('reverse')
dll.print_reverse()

print('\n5. set_head')
print(dll.set_head(3))
dll.print()
print(dll.set_head(11))
dll.print()
print('reverse')
dll.print_reverse()

print('\n6. access')
print(dll.access(0))
print(dll.access(4))

print('\n7. insert')
print(dll.insert(0,1))
dll.print()
dll.print_reverse()
print('--------------------------')
print(dll.insert(1,10))
dll.print()
dll.print_reverse()
print('--------------------------')
print(dll.insert(3,11))
dll.print()
dll.print_reverse()
print('--------------------------')
print('reverse')
dll.print_reverse()

print('\n8. remove')
print(dll.remove(0))
dll.print()
dll.print_reverse()
print('----')
print(dll.remove(4))
dll.print()
dll.print_reverse()
print('----')
print(dll.remove(3))
dll.print()
dll.print_reverse()
print('----')
print(dll.remove(9))
dll.print()

print('----')
dll.print_reverse()