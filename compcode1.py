#PYTHON CODE
'''Code for Bubble sort, Selection sort, Insertion sort'''

import time
import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Measure execution time
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

# Generate a random list of numbers
size = 1000  # Adjust size for performance comparison
random_list = [random.randint(0, 10000) for _ in range(size)]

# Copy the list for fair comparisons
lists = {"Bubble Sort": random_list[:],
         "Selection Sort": random_list[:],
         "Insertion Sort": random_list[:],
         "Timsort (Python sorted)": random_list[:]}

# Measure performance
results = {}
for name, lst in lists.items():
    if name == "Timsort (Python sorted)":
        start_time = time.time()
        sorted(lst)  # Python's built-in sort
        results[name] = time.time() - start_time
    else:
        results[name] = measure_time(globals()[name.lower().replace(" ", "_")], lst)

# Display results
for algo, time_taken in results.items():
    print(f"{algo}: {time_taken:.6f} seconds")
