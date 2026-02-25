import random


def randomized_quicksort(arr):

   # Sorts an array using the Randomized Quicksort algorithm.

    if len(arr) <= 1:
        return arr
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]

        less_than_pivot = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        greater_than_pivot = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]

        return randomized_quicksort(less_than_pivot) + [pivot] + randomized_quicksort(greater_than_pivot)


data = [10, 7, 8, 9, 1, 5]
print("Unsorted:", data)
print("Sorted:", randomized_quicksort(data))