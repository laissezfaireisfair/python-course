import argparse

parser = argparse.ArgumentParser(description='Pascal triangle')
parser.add_argument('size', type=int, help='Size of triangle')

args = parser.parse_args()
size = args.size

triangle = [[0] * length for length in range(1, size + 1)]
triangle[0][0] = 1

for i in range(1, size):
    triangle[i][0] = 1
    triangle[i][i] = 1
    for j in range(1, i):
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

string = '\n'.join([' '.join([str(num) for num in line]) for line in triangle])
print(string)
    