import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def prepend(self, value):
        if self.length != self.capacity: 
            idx = self.length
            while idx > 0:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[0] = value

        else: # 배열이 꽉 찬 상태일 경우
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i + 1] = self.array[i]
            new_array[0] = value
            self.array = new_array

        self.length += 1
            
    def append(self, value):
        if self.length != self.capacity: 
            self.array[self.length] = value

        else: # 배열이 꽉 찬 상태일 경우
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            new_array[self.length] = value
            self.array = new_array

        self.length += 1

    def set_head(self, index):
        if (index >= self.length):
            print('out of range')
            return
        for i in range(self.length-index):
            self.array[i] = self.array[i+index]
        self.length -= index

    def access(self, index):
        if (index >= self.length):
            print('out of range')
            return
        print(self.array[index])

    def insert(self, index, value):
        if (index >= self.length):
            print('out of range')
            return

        if self.length != self.capacity: 
            idx = self.length
            while idx >= index:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[index] = value
        else: # 배열이 꽉 찬 상태일 경우
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                if (i < index):
                    new_array[i] = self.array[i]
                else:
                    new_array[i+1] = self.array[i]
            new_array[index] = value
            self.array = new_array
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            print('out of range')
            return
        for i in range(index, self.length):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def print(self):
        if self.length == 0:
            print('List is empty')
            return
        for i in range(self.length):
            print(self.array[i], end=' ')
        # print('length', self.length, self.capacity)
        return 

array_list = ArrayList(4)
print('\n0. print')
array_list.print()

print('\n1. is_empty')
print(array_list.is_empty())

print('\n2. prepend')
for i in range(4):
    array_list.prepend(i)
array_list.print()
print()
array_list.prepend(8)
array_list.print()

print('\n\n3. append')
for i in range(3):
    array_list.append(9)
array_list.print()
print()
array_list.append(10)
array_list.print()

print('\n\n4. set_head')
array_list.set_head(5)
array_list.print()

print('\n\n5. access')
array_list.access(2)
array_list.access(3)
array_list.access(8)

print('\n6. insert')
array_list.insert(5,8)
array_list.print()
array_list.insert(1,8)
array_list.print()

print('\n7. remove')
array_list.remove(1)
array_list.print()
print()
array_list.remove(100)
array_list.print()

