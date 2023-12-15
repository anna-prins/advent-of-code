import sys

with open(sys.argv[1]) as data:
    file = data.read()
lines = [[int(i) for i in s.split()] for s in file.split('\n')]

def find_diffs(line):
    sum = 0
    for char in line:
        sum += char != 0
    if sum == 0:
        return 0
    new_line = []
    for index in range(len(line)-1):
        diff = line[index+1]-line[index]
        new_line.append(diff)
    return line[-1] + find_diffs(new_line)

part_1_sum = 0
for line in lines:
    part_1_sum += find_diffs(line)

part_2_sum = 0
for line in lines:
    part_2_sum += find_diffs(line[::-1])

print(part_1_sum)
print(part_2_sum)