from data_structures.linked_list import Node

class InvalidOperationError(BaseException):
  pass

class Stack:
  def __init__(self, node = None):
    self.top = node
    self.counter = 0


  def push(self, value):
    node = Node(value)
    node.next = self.top
    self.top = node
    self.counter += 1

  def pop(self):
    if self.top is None:
      raise InvalidOperationError("your stack is empty")
    node = self.top
    self.top = self.top.next
    self.counter -= 1
    return node.value

  def peek(self):
    if self.top is None:
      raise InvalidOperationError("your stack is empty")
    return self.top.value

  def is_empty(self):
    True if self.top is None else False
    # if self.top is None:
    #   return True
    # else:
    #   return False


      