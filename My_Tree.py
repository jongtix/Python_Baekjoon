class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def pre_order_traversal(self, node):
        print(node, end='')
        if not node.left  == None : self.pre_order_traversal(node.left)
        if not node.right == None : self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if not node.left  == None : self.in_order_traversal(node.left)
        print(node, end='')
        if not node.right == None : self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if not node.left  == None : self.post_order_traversal(node.left)
        if not node.right == None : self.post_order_traversal(node.right)
        print(node, end='')

    def make_root(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node