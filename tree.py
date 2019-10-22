from queue import Queue

class BinaryTree:

    def __init__(self):
        self._root = None

    def __repr__(self):
        current = self._root
        result = []
        while current:
            left = current.left
            right = current.right
            result.append(f'{left}, {right}')
            current = left
        return ' -> '.join(result)

    def insert_node(self, value):
        """
        Public insert method
        Allows input to be just value, checks root and passes parameters to
        private method.
        """
        if self._root is None:
            self._root = TreeNode(value)
        else:
            self._insert(self._root, value)

    def _insert(self, node, value):
        '''
        Prive insert method, inserts a node into the binarytree
        :param value: the value of the node you're looking to insert
        :param node: the node, under which it will the new node will be inserted
        '''

        if value > node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)

        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def breadth_first_search(self):
        root = self._root
        order = Queue()
        nodes = []

        order.put(root)

        while order.qsize() > 0:

            item = order.get()
            nodes.append(item)

            if item.left:
                order.put(item.left)

            if item.right:
                order.put(item.right)

        return nodes

    def depth_first_search(self, value):
        ...


class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node:{self.value}"


t = BinaryTree()
t.insert_node(1)
t.insert_node(2)
t.insert_node(3)
t.insert_node(4)
t.insert_node(5)


bfs = t.breadth_first_search()
print(bfs)

    # depth_first_search
    #     recursion
