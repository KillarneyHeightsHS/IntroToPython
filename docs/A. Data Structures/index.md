# Data Structures

## Introduction to Data Structures
Data structures are fundamental concepts in computer science that organise and store data efficiently. They provide a way to access, search, insert, and delete data in an organised manner. Common data structures include arrays, linked lists, stacks, queues, trees, graphs, and hash tables.

## Arrays
An array is a collection of elements of the same type stored at contiguous memory locations. Each element can be accessed using its index, which starts from 0. Arrays are useful for storing fixed-size collections of data.

### Example in Python: 
```python
# Creating an array of integers
my_array = [1, 2, 3, 4, 5]

# Accessing elements by index
print(my_array[0])  # Output: 1
print(my_array[3])  # Output: 4
# Modifying elements
my_array[2] = 10
print(my_array)  # Output: [1, 2, 10, 4, 5]
```

## Linked Lists
A linked list is a linear data structure where each element (node) contains a value and a reference to the next node. Unlike arrays, linked lists do not require contiguous memory locations. They are useful for dynamic data structures that can grow or shrink at runtime.

### Example in Python: 
```python
# Creating a simple linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: Node):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def remove(self, value: Node):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current and current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
```

# Example usage
```python
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.remove(1)
```
The result of the above code is that the linked list contains only the value `2`.

## 











head = Node(1)
second_node = Node(2)
third_node = Node(3)

head.next = second_node
second_node.next = third_node
```














