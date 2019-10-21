class BinaryTree:

    def __init__(self):
        self._head = None

    def __repr__(self):
        current = self._head
        result = []
        while current:
            left = current.left
            right = current.right
            result.append(f'{left}, {right}')
        return ' -> '.join(result)

    def insert_node(self, value, node=None):
        """
        inserts a node into the binarytree
        :param value: the value of the node you're looking to insert
        :param node: the node, under which it will the new node will be inserted
        """
        if node is None:
            self._head = TreeNode(value)

        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_node(value, node.left)

        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_node(value, node.left)

    def bredth_first_search(self, value):
        ...

    def depth_first_search(self, value):
        ...


class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node:{self.val}"






    # depth_first_search
    #     recursion
    #
    # breadth_first_search
    #     queue
