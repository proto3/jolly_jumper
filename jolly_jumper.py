line = raw_input()

words = line.split()

numbers = [int(i) for i in words]

diff = [i-j for i,j in zip(numbers[:-1], numbers[1:])]

diff.sort()

print(range(1, len(numbers)) == diff)
