class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        s = ''
        def recursive(node):
            nonlocal s
            s += str(node.value) + ' '
            if node.left:
                recursive(node.left)
            if node.right:
                recursive(node.right)

        s = '['
        recursive(self.root)
        s += ']'
        print(s)
    
    def inorder(self):
        s = ''
        def recursive(node):
            nonlocal s
            if node.left:
                recursive(node.left)
            s += str(node.value) + ' '
            if node.right:
                recursive(node.right)

        s = '['
        recursive(self.root)
        s += ']'
        print(s)
    
    def postorder(self):
        s = ''
        def recursive(node):
            nonlocal s
            if node.left:
                recursive(node.left)
            if node.right:
                recursive(node.right)
            s += str(node.value) + ' '

        s = '['
        recursive(self.root)
        s += ']'
        print(s)

    def bfs(self, value):
        queue = []
        isFound = False
        queue.append(self.root)

        while queue:
            node = queue[0]
            del queue[0]
            if node.value == value:
                isFound = True
                return isFound
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return isFound
    
    def dfs(self, value):
        isFound = False
        def recursive(node):
            nonlocal isFound
            if node.value == value:
                isFound = True
                return
            if isFound is True:
                return
            if node.left is not None:
                recursive(node.left)
            if node.right is not None:
                recursive(node.right)
        
        recursive(self.root)
        return isFound


tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()

print(tree.dfs(4))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))