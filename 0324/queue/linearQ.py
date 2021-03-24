import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            return False # Overflow
        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        if self.front == self.rear:
            return None # Underflow
        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.front == self.rear:
            return None # Underflow
        return self.array[self.front]

    def print(self):
        if self.rear == 0:
            print('[]')
        else:
            for i in range(self.front, self.rear):
                print(self.array[i], end=' ')
    

linearQ = LinearQueue(10)
linearQ.print()

linearQ.put(1)
linearQ.print()

print()
for i in range(2,5):
    linearQ.put(i)
linearQ.print()

print()
print(linearQ.peek())

for i in range(6):
    print(linearQ.get(), end=' ')
print()
linearQ.print()

linearQ.put(10)
print(linearQ.peek())
linearQ.print()