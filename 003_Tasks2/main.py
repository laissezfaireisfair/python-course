import random as rand
import functools as func
import re


def is_palindrome(string: str) -> bool:
    for i, s in enumerate(string):
        if string[len(string) - i - 1] != s:
            return False
    return True


def find_largest_word(string: str) -> str:
    words = string.split(' ')
    return func.reduce(lambda a, x: x if len(x) > len(a) else a,
                       words,
                       '')


def count_odds_and_even() -> (int, int):
    rand_ints = rand.choices(range(1000), k=100)
    return func.reduce(lambda a, x: (a[0], a[1] + 1) if x % 2 == 0 else (a[0] + 1, a[1]),
                       rand_ints,
                       (0, 0))


def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


class Stats:
    def __init__(self, lines: int, symbols: int, words: int):
        self.lines = lines
        self.symbols = symbols
        self.words = words

    def __str__(self):
        return (f'Text stats:\n'
                f'Lines: {self.lines}\n'
                f'Words: {self.words}\n'
                f'Symbols: {self.symbols}')


def count_text_stats(text: str) -> Stats:
    filtered = list(filter(lambda s: s != '\n', text))
    symbols_count = len(filtered)
    lines_count = len(text.split('\n'))
    words_count = len(re.split('[ \n]', text))
    return Stats(lines_count, symbols_count, words_count)


def progression_gen(b: int, q: int):
    val = b
    while True:
        val *= q
        yield val


def main():
    print(is_palindrome('abccba'))
    print(find_largest_word('a ba bcab bgh'))
    print(count_odds_and_even())
    print(fib(6))
    print(count_text_stats('a b baubub\n'
                           'eedw wedwd'))
    val = progression_gen(1, 2)
    for i in range(15):
        print(val)


main()
