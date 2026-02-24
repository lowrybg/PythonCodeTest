import random


def fisher_yates_shuffle(arr):

    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)

        arr[i], arr[j] = arr[j], arr[i]

    return arr


my_list = [1, 2, 3, 4, 5, 6, 7]
print("Original:", my_list)
print("Shuffled:", fisher_yates_shuffle(my_list))