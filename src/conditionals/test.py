def add(a: int, b: int):
    print('int')
    return a + b
def add(a: float, b: float):
    print('float')
    return a + b
def add(a: str, b: str):
    print('str')
    return a + b

print(add(1, 2)) # Output: 3
print(add(1.5, 2.5)) # Output: 4.0
print(add("Hello", "World")) # Output: HelloWorld