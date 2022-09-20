from data_structures.linked_list import Node


class InvalidOperationError(BaseException):
  pass


class Queue:

  def __init__(self):
    self.front = None
    self.rear = None
    self.counter = 0
  
  def enqueue(self, value):
    node = Node(value)
    if self.front is None:
        self.front = node
        self.rear = node
    else:
        self.rear.next = node
        self.rear = node
    self.counter +=1
  
  def dequeue(self):
    if self.is_empty():
        raise InvalidOperationError("Your queue is empty")
    node = self.front
    self.front = self.front.next
    self.counter -= 1
    return node.value

  def peek(self):
    if self.is_empty():
        raise InvalidOperationError("Your queue is empty")
    return self.front.value

  def is_empty(self):
    return True if self.front is None else False
    # if self.front is None:
    #     return True
    # else:
    #     return False
