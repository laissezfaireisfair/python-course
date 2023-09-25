import numpy as np
import functools as ft


def add_occurrence(acc: dict, x: int) -> dict:
    if x in acc:
        acc[x] += 1
    else:
        acc[x] = 1
    return acc


def sort_by_frequency(items):
    occurrences = ft.reduce(add_occurrence, items, {})
    np.expand_dims(items, 1)
    for i in items:
        items[i:1] = occurrences[i]
    ordered = np.argsort(items, axis=1)
    return ordered


example1 = np.array([3, 1, 2, 3, 2, 3])
print(f'{example1} sorted by frequency: {sort_by_frequency(example1)}')
