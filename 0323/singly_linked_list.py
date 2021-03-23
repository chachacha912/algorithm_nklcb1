class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def is_empty(self):
		if self.head == None:
			return True
		return False

	def prepend(self, value):
		if self.head == None:
			self.head = Node(value,None)
		else:
			self.head = Node(value, self.head)

	def append(self, value):
		if self.head == None:
			self.head = Node(value, None)
		else:
			node = self.head
		while node.next:
			node = node.next
		node.next = Node(value, None)

	def set_head(self, index):
		node = self.head
		for i in range(index):
			if node == None:
				return False
			node = node.next
		self.head = node
		return True

	def access(self, index):
		node = self.head
		for i in range(index):
			if node == None:
				return False
			node = node.next
		return node.value

	def insert(self, index, value):
		if self.head == None and index > 0:
			return False

		if index == 0:
			self.prepend(value)
			return True

		node = self.head
		prev_node = None
		for i in range(index):
			if node == None:
				return False
			prev_node = node
			node = node.next

		prev_node.next = Node(value, node)
		return True

	def remove(self, index):
		if index == 0:
			if self.head:
				self.head = self.head.next
				return True
			return False

		node = self.head
		prev_node = None
		for i in range(index):
			if node == None:
				return False
			prev_node = node
			node = node.next

		if node == None:
			return False

		prev_node.next = node.next
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


sll = SinglyLinkedList()
print('\n0. print')
sll.print()

print('\n1. is_empty')
print(sll.is_empty())

print('\n2. prepend')
sll.prepend(1)
sll.prepend(2)
sll.print()

print('\n3. append')
for i in range(3):
    sll.append(i+3)
sll.print()

print('\n4. set_head')
print(sll.set_head(3))
sll.print()
print(sll.set_head(3))
sll.print()

print('\n5. access')
print(sll.access(0))
print(sll.access(5))

print('\n6. insert')
print(sll.insert(0,1))
sll.print()
print(sll.insert(2,7))
sll.print()
print(sll.insert(5,4))
sll.print()

print('\n7. remove')
print(sll.remove(0))
sll.print()
print(sll.remove(1))
sll.print()
print(sll.remove(10))
sll.print()