input = open('input.txt', 'r')
output = open('output.txt', 'w')
a, b = input.read().split()
output.write(str(int(a) + int(b) ** 2))