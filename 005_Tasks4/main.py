import numpy as np

import random as rand


def sort_by_frequency(items: [int]) -> None:
    unique, counts = np.unique(items, return_counts=True)
    occurrences = dict(zip(unique, counts))
    items.sort(key=lambda x: -occurrences[x])


example1 = [2, 3, 2, 1, 2, 1]
print(example1)
sort_by_frequency(example1)
print(f'Sorted by frequency: {example1}\n')


def get_unique_colors(pic):
    return np.unique(pic).size


h = 10
w = 20
example2 = np.array([[rand.randint(0, 255) for _ in range(w)] for _ in range(h)])
print(example2)
unique_colors = get_unique_colors(example2)
print(f'Unique colors: {unique_colors}\n')

