import math
import os
import random as rand


def get_digit_sum(num: int) -> int:
    num_str = str(num)
    return sum([int(s) for s in num_str])


def task1() -> None:
    rand_num = rand.randint(100, 999)
    digits_sum = get_digit_sum(rand_num)
    print(f'Rand 3-digit number: {rand_num}, digit sum: {digits_sum}')


def task2() -> None:
    rand_num = rand.randint(0, 6 * 10 ** 23)
    digits_sum = get_digit_sum(rand_num)
    print(f'Rand number: {rand_num}, digit sum: {digits_sum}')


def task3() -> None:
    sphere_radius = rand.randint(0, 100)
    surface_area = 4 * math.pi * sphere_radius ** 2
    volume = 4 / 3 * math.pi * sphere_radius ** 3
    print(f'Sphere with radius {sphere_radius} have surface area {surface_area} and volume {volume}')


def is_year_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def task4() -> None:
    year = rand.randint(0, 4046)
    is_leap = is_year_leap(year)
    print(f'Year {year} is {"" if is_leap else "not "}leap')


def task5() -> None:
    up_limit = 10 ** 5
    nums = range(up_limit + 1)
    is_prime_by_num = [True if n > 1 else False for n in nums]

    for i in nums[2:]:
        if is_prime_by_num[i]:
            for j in nums[2 * i::i]:
                is_prime_by_num[j] = False

    primes_str = ', '.join([str(i) for i in nums if is_prime_by_num[i]])
    print(f'Primes up to {up_limit}: {primes_str}')


def task6() -> None:
    initial_sum = rand.randint(1, 10 ** 7)
    duration_years = rand.randint(1, 15)
    final_sum = initial_sum * 1.1 ** duration_years
    print(f'Initial sum {initial_sum} after {duration_years} years will be {final_sum}')


def print_path_content(path) -> None:
    for root, dirs, files in os.walk(path):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print_path_content(os.path.join(root, name))


def task7() -> None:
    try:
        path = os.path.join('d:\\', 'Films')
        print_path_content(path)
    except Exception as exception:
        print(exception)


task1()
task2()
task3()
task4()
task5()
task6()
task7()
