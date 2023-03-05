

with open('day8.txt', 'r') as file:
    puzzle = file.read().split('\n')

text = "".join(puzzle)
total = len(text)

result = 0
for string in puzzle:
    result += len(eval(string))

print(total - result)


