import argparse
import random as rand


def bubble_sort(nums: [int]) -> None:
    while True:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                changed = True

        if not changed:
            break


parser = argparse.ArgumentParser(description='Bubble sort')
parser.add_argument('size', type=int, help='Size of sorted array')

args = parser.parse_args()
size = args.size

# alphabet = [0, 1]
alphabet = range(1000)
values = rand.choices(alphabet, k=size)

original_values_str = ', '.join([str(i) for i in values])
print(original_values_str)

bubble_sort(values)

print(', '.join([str(i) for i in values]))
