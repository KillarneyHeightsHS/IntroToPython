# Algorithms
There are some common algorithms that you should understand. These include sorting algorithms, searching algorithms, dynamic programming, and graph algorithms. Each of these algorithms has its own strengths and weaknesses, so it's important to understand when to use each one.

!!! Note
    More general information about algorithms can be found in the NSW Software Engineering reference material. The content here is more about the implementation in Python.
    
    - [Algorithms](https://mr-bev.github.io/software-engineering-stage6-nsw/fundamentals/algorithms/){:target="_blank"}
    - [Algorithm Complexity | BigO](https://mr-bev.github.io/software-engineering-stage6-nsw/fundamentals/big_o/){:target="_blank"}


## Performance Analysis
Performance analysis is the process of measuring and analysing the efficiency of an algorithm or program. This includes identifying bottlenecks, optimising code, and choosing the right data structures. Performance analysis is important because it can help you improve the speed and scalability of your applications.

A commonly used unit for measuring performance is Big O notation, which describes the upper bound of an algorithm's time or space complexity as the input size grows. For example, an algorithm with a time complexity of `O(n^2)` will take twice as long to run when the input size doubles.

There are many ways to profile your python code. The quickest way is to read the code and rationalise the data structures used, but this can be time-consuming for large codebases.

- You can use `cProfile` module which is built into Python. It provides a high-level interface for profiling Python programs. You can use it to measure the time taken by different functions or code blocks, and identify which parts of your program are taking the most time.

<need example>

- You can use `timeit` module which is also built into Python. It provides a simple way to measure the execution time of small code snippets. You can use it to compare the performance of different algorithms or implementations.

<need example>

- Pytest is a popular testing framework for Python, but it also provides profiling capabilities. You can use it to measure the performance of your tests and identify which parts of your code are taking the most time. There is a handy addon called `pytest-profiling` which will generate a graphical report showing the performance of your tested code. Internally it uses `cProfile` to collect profiling data.

<need  example>

## Sorting Algorithms
Sorting algorithms are used to arrange a list of items in a specific order. There are many different types of sorting algorithms, including:

- bubble sort
- insertion sort
- selection sort
- merge sort
- quicksort
- heapsort

Each one has its own time complexity, which is the amount of time it takes to run as a function of the size of the input. For example, bubble sort has a time complexity of `O(n^2)`, while merge sort has a time complexity of `O(n log n)`. The choice of sorting algorithm depends on the specific requirements of your application.

!!! tip
    Using a pack of cards can help you understand the concept of sorting algorithms. Mix up the cards and then try to sort them using different sorting algorithms. This can help you understand how each algorithm works and which one is most efficient.

### Bubble Sort
- Bubble sort is a simple and intuitive sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. It gets its name from the way smaller elements "bubble" to the top of the list. 
```python
import timeit

def bubble_sort(arr):
    ''' Note that is modifies the array in-place. '''
    n = len(arr)
    for i in range(n - 1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
            
if __name__ == "__main__":
    input = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted array is:", list(input))
    bubble_sort(input)
    print ("Sorted array is:", input)

    result = timeit.timeit(lambda: bubble_sort(list(input)))
    print(f"Time taken to sort the array using Bubble Sort: {result} seconds for 100000 runs.")
```
- Bubble sort has a time complexity of `O(n^2)`, which makes it inefficient for large lists. However, it is easy to understand and implement.

In the code there are a few things you should be aware of:
- As the bubble sort is done in-place you need to provide a copy of the input array when calling `timeit.timeit` so that the original array is not modified.
- The default number of runs for `timeit.timeit` is 1,000,000. If you want to change this you can do so by passing the `number` parameter.
- The prints are a separate step and not part of timing analysis as printing to the screen is time consuming and would influence the result

!!! example "Try it yourself!"
    - Modify the code above so that it doesn't make a copy of the list, does the time taken to sort the array change? Why or why not?
    - Change the number of runs for `timeit.timeit` and observe how it affects the result.
    - Try creating a bigger lists using `random.sample()`, and see how bubble sort performs on them.
    - Include print statements in the `bubble_sort` method to see how it impacts the time measurement.


### Insertion Sort
- Insertion sort has a time complexity of `O(n^2)`, but it is more efficient than bubble sort for small lists or nearly sorted lists. It works by building the final sorted array one item at a time, inserting each new element into its correct position in the already-sorted portion of the array.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr
```




### Selection Sort

### Merge Sort

### Quicksort

### Heapsort

## Search Algorithms
The following search algorithms are covered in this section:
- Linear Search
- Binary Search
- Depth-First Search (DFS)
- Breadth-First Search (BFS)



