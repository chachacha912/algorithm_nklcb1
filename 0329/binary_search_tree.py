class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'

        return node, parent, direction 

    def insert(self, value):
        node, parent, direction = self.__search(value)

        if parent is None:
            self.root = Node(value)
            return True
            
        if node: 
            return False # 중복 처리
        elif direction == 'left':
            parent.left = Node(value)
        else:
            parent.right = Node(value) 

    def search(self, value):
       node, _, _ = self.__search(value)
       return node

    def remove(self, value):
        node, parent, direction = self.__search(value)
        if node is None:
            return False
        
        if node.left is None and node.right is None: # (a) 자식 노드가 없는 노드는 단순히 삭제한다.
            if parent is None: # 루트 노드일 경우
                self.root = None
            elif direction == 'left':
                parent.left = None
            else:
                parent.right = None

        elif node.left and node.right: # (b) 두 자식이 모두 있는 경우, 왼쪽(오른쪽) Sub-Tree에서 가장 오른쪽(왼쪽)에 있는 노드로 대체한다.
            last_parent = node
            last = node.left

            while last.right:
                last_parent = last
                last = last.right
            
            if last_parent == node:
                last_parent.left = last.left
            else:
                last_parent.right = last.left
                last.left = node.left

            last.right = node.right
            
            if parent is None:
                self.root = last
            elif direction == 'left':
                parent.left = last
            else:
                parent.right = last

            return True


        else: # (c) 자식이 하나만 있으면, 자식 노드로 대체한다.
            if parent is None:
                self.root = node.left if node.left else node.right
            elif direction == 'left':
                parent.left = node.left if node.left else node.right
            else:
                parent.right = node.left if node.left else node.right


bst = BinarySearchTree()

# import random
# x = list(range(5))
# random.shuffle(x)
x = [5,3,1,4,2,18,13,9,7,11,6,10,15,14,16]
for elem in x:
    bst.insert(elem)
bst.root.display()

print(bst.search(4))
print(bst.search(8))
print(bst.search(0))

bst.remove(14)
bst.root.display()

bst.remove(15)
bst.root.display()

bst.remove(13)
bst.root.display()
