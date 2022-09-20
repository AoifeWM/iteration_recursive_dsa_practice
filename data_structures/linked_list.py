from data_structures.node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def add(self, value):
    node = Node(value)

    if self.head is None:
      self.head = node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = node

  
