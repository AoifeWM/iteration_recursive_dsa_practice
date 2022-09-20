from data_structures.linked_list import Node

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def add(self, value, node):
    new_node = Node(value)

    if self.root is None:
      self.root = new_node
      return

    if new_node.value < node.value:
      if node.left is None:
        node.left = new_node
      else:
        self.add(value, node.left)
    elif new_node.value > node.value:
      if node.right is None:
        node.right = new_node
      else:
        self.add(value, node.right)


      