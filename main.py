from data_structures.node import Node
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree
from data_structures.binary_search_tree import BinarySearchTree


# Iterate a linked list iteratively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively(input_linked_list):
    current = input_linked_list.head
    if not current:
        return None
    top = current.value
    while current:
        if current.value > top:
            top = current.value
        current = current.next
    return top

# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and return the smallest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_iteratively_small(input_linked_list):
    current = input_linked_list.head
    if not current:
        return None
    low = current.value
    while current:
        if current.value < low:
            low = current.value
        current = current.next
    return low


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list iteratively and remove duplicate values
# input_linked_list (7)->(2)->(13)->(2)->(9)->(3)->(9)

def iterate_linkedlist_iteratively_duplicates(input_linked_list):
    current = input_linked_list.head.next
    if not current:
        return None
    prev = input_linked_list.head
    found = [input_linked_list.head.value, ]
    while current:
        if current.value in found:
            prev.next = current.next
            current = current.next
        else:
            found.append(current.value)
            prev = current
            current = current.next
    return found


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list, and return the value furthest removed from zero
# input_linked_list (7)->(2)->(13)->(-9)->(3)->(-21)

def iterate_linkedlist_furthest_from_zero(input_linked_list):
    current = input_linked_list.head
    if not current:
        return None
    far = current.value
    while current:
        if abs(current.value) > abs(far):
            far = current.value
        current = current.next
    return far


# Iterate a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively(input_node, largest=None):
    if largest is None:
        largest = input_node.value
    if input_node.value > largest:
            largest = input_node.value
    if input_node.next:
        largest = iterate_linkedlist_recursively(input_node.next, largest)
    return largest


# ##################### NEW #####################################
# Write a test to cover this
# Iterate through a linked list recursively and return the largest value
# input_linked_list (7)->(2)->(13)->(9)->(3)
def iterate_linkedlist_recursively_smallest(input_node, smallest=None):
    if smallest is None:
        smallest = input_node.value
    if input_node.value < smallest:
        smallest = input_node.value
    if input_node.next:
        smallest = iterate_linkedlist_recursively_smallest(input_node.next, smallest)
    return smallest


# Iterate a stack iteratively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_iteratively(input_stack):
    current = input_stack.top
    if not current:
        return None
    large = current.value
    while current:
        if current.value > large:
            large = current.value
        current = current.next
    return large


# Iterate a stack recursively and return the largest value
# input_stack (7)->(2)->(13)->(9)->(3)
def iterate_stack_recursively(input_stack, largest=None):
    top = input_stack.top
    return iterate_linkedlist_recursively(top)


# Iterate a queue iteratively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_iteratively(input_queue):
    current = input_queue.front
    if not current:
        return None
    large = current.value
    while current:
        if current.value > large:
            large = current.value
        current = current.next
    return large

# Iterate a queue recursively and return the largest value
# input_queue (7)->(2)->(13)->(9)->(3)
def iterate_queue_recursively(input_queue, largest=0):
    front = input_queue.front
    return iterate_linkedlist_recursively(front)


# Perform a Pre-Order, In-Order, and Post-Order traversal of a binary tree.
#                       4
#                     /   \
#                   7      18
#                 /   \   /   \
#                3     1 5     11
#
# Pre-Order Traveral
# expected [4, 7, 3, 1, 18, 5, 11]
def pre_order_traversal(input_node, values=[]):
    if not input_node:
        return
    values.append(input_node.value)
    pre_order_traversal(input_node.left, values)
    pre_order_traversal(input_node.right, values)
    return values


# In-Order Traveral
# expected [3, 7, 1, 4, 5, 18, 11]
def in_order_traversal(input_node, values=[]):
    if not input_node:
        return
    in_order_traversal(input_node.left, values)
    values.append(input_node.value)
    in_order_traversal(input_node.right, values)
    return values


# Post-Order Traveral
# expected [3, 1, 7, 5, 11, 18, 4]
def post_order_traversal(input_node, values=[]):
    if not input_node:
        return
    post_order_traversal(input_node.left, values)
    post_order_traversal(input_node.right, values)
    values.append(input_node.value)
    return values


# Level Order, or Breadth First, Traversal
# expected [4, 7, 18, 3, 1, 5, 11]
def level_order_traversal(input_tree):
    q = Queue()
    searched = []
    if input_tree.root:
        q.enqueue(input_tree.root)
    while q.front:
        current = q.dequeue()
        searched.append(current.value)
        if current.left:
            q.enqueue(current.left)
        if current.right:
            q.enqueue(current.right)
    return searched



# ##################### NEW #####################################
# Write a test to cover this
# Binary Search Tree for contains
#                       7
#                     /   \
#                  -3      13
#                 /   \   /   \
#               -21     5 9    17
#
# Given a bst, return value the furthest removed from zero
def bst_furthest(input_tree):
    current = input_tree.root
    while current.right:
        current = current.right
    high = current.value
    current = input_tree.root
    while current.left:
        current = current.left
    low = current.value
    return low if abs(low) > high else high


# Binary Search Tree for contains
#                       7
#                     /   \
#                   3      13
#                 /   \   /   \
#                1     5 9     17
#
# Given a value return true or false if it's contained within the binary search tree
def bst_contains(input_tree, value):
    current = input_tree.root
    while current:
        if current.value == value:
            return True
        elif value < current.value:
            current = current.left
        else:
            current = current.right

    return False


# -----------------------------------------------------
# -----------------------------------------------------
# ----------------- TEST RUNNER STUFF -----------------
# -----------------------------------------------------
# -----------------------------------------------------


def run_tests():
    # Linked List Tests
    input_linked_list = make_linked_list()
    print("LinkedList Iteratively Largest: {}".format(iterate_linkedlist_iteratively(input_linked_list)))
    print("LinkedList Iteratively Smallest: {}".format(iterate_linkedlist_iteratively_small(input_linked_list)))
    print("LinkedList Iteratively Remove Duplicates: {}".format(
        iterate_linkedlist_iteratively_duplicates(input_linked_list)))
    print("LinkedList Iteratively furthest from 0: {}".format(
        iterate_linkedlist_furthest_from_zero(input_linked_list)))
    print("LinkedList Recursively largest: {}".format(iterate_linkedlist_recursively(input_linked_list.head)))
    print("LinkedList Recursively smallest: {}".format(iterate_linkedlist_recursively_smallest(input_linked_list.head)))

    # Stack Tests
    input_stack = make_stack()
    print("Stack Iteratively: {}".format(iterate_stack_iteratively(input_stack)))
    input_stack = make_stack()
    print("Stack Recursively: {}".format(iterate_stack_recursively(input_stack)))

    # Queue Tests
    input_queue = make_queue()
    print("Queue Iteratively: {}".format(iterate_queue_iteratively(input_queue)))
    input_queue = make_queue()
    print("Queue Recursively: {}".format(iterate_queue_recursively(input_queue)))

    # BinaryTree Order Traversal Tests
    input_binary_tree = make_binary_tree()
    print("Pre-Order Traversal: \n{}".format(pre_order_traversal(input_binary_tree.root)))
    print("In-Order Traversal: \n{}".format(in_order_traversal(input_binary_tree.root)))
    print("Post-Order Traversal: \n{}".format(post_order_traversal(input_binary_tree.root)))
    print("Level-Order Traversal: \n{}".format(level_order_traversal(input_binary_tree)))

    # Binary Search Tree Contains and Depth Search Tests
    input_binary_search_tree = make_binary_search_tree()
    print("Binary Search Tree Breadth First: {}".format(level_order_traversal(input_binary_search_tree)))
    print("Binary Search Tree Contains 13: {}".format(bst_contains(input_binary_search_tree, 13)))
    print("Binary Search Tree Contains 11: {}".format(bst_contains(input_binary_search_tree, 11)))
    print("Binary Search Tree Furthest Value From 0: {}".format(bst_furthest(input_binary_search_tree)))



# helper methods to instatiate the datastructures
def make_linked_list():
    input_linked_list = LinkedList()
    input_linked_list.add(7)
    input_linked_list.add(2)
    input_linked_list.add(2)
    input_linked_list.add(9)
    input_linked_list.add(2)
    input_linked_list.add(13)
    input_linked_list.add(9)
    input_linked_list.add(7)
    input_linked_list.add(3)
    return input_linked_list


def make_stack():
    input_stack = Stack()
    input_stack.push(7)
    input_stack.push(2)
    input_stack.push(13)
    input_stack.push(9)
    input_stack.push(3)
    return input_stack


def make_queue():
    input_queue = Queue()
    input_queue.enqueue(7)
    input_queue.enqueue(2)
    input_queue.enqueue(13)
    input_queue.enqueue(9)
    input_queue.enqueue(3)
    return input_queue


def make_binary_tree():
    input_binary_tree = BinaryTree()
    node_a = Node(4)
    node_b = Node(7)
    node_c = Node(18)
    node_d = Node(3)
    node_e = Node(1)
    node_f = Node(5)
    node_g = Node(11)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    input_binary_tree.root = node_a
    return input_binary_tree


def make_binary_search_tree():
    input_binary_search_tree = BinarySearchTree()
    input_binary_search_tree.add(7, None)
    root = input_binary_search_tree.root
    input_binary_search_tree.add(-33, root)
    input_binary_search_tree.add(28, root)
    input_binary_search_tree.add(-12, root)
    input_binary_search_tree.add(13, root)
    input_binary_search_tree.add(-9, root)
    input_binary_search_tree.add(-123, root)
    input_binary_search_tree.add(113, root)
    return input_binary_search_tree


run_tests()
