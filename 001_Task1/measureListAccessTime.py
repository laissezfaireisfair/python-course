import time


def measure_access_time(lst: [int], position: int):
    elem_access_begin = time.perf_counter_ns()
    elem = lst[position]
    elem_access_end = time.perf_counter_ns()
    return elem_access_end - elem_access_begin


size = 10**7

numbers = [i for i in range(size)]

secondElemAccessElapsed = measure_access_time(numbers, 1)
midElemAccessElapsed = measure_access_time(numbers, size // 2)
preLastElemAccessElapsed = measure_access_time(numbers, size - 2)

print(f'Second elem access time: {secondElemAccessElapsed} ns')
print(f'Mid elem access time: {midElemAccessElapsed} ns')
print(f'Pre-last elem access time: {preLastElemAccessElapsed} ns')
