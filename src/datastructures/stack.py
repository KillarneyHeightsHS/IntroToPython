# Custom Stack class
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print("Stack:", self.items)

# Example usage
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.display()  # Stack: ['A', 'B', 'C']


def reverse(word):
    # -- your code goes here --
    pass

def is_balanced(brackets):
    # -- your code goes here --
    pass


reverse("Killarney") == "eyrenllaK"
reverse("Madam Im Adam") == "madaM mi maMlaD"

is_balanced("((()))") == True
is_balanced("([]){}") == True
is_balanced("[[])") == False
