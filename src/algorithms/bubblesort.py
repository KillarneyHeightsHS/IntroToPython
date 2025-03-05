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
