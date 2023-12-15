import sys

with open(sys.argv[1]) as data:
    file = data.read()
lines = file.split('\n')

patterns = []
pattern = []
for line in lines:
    if line != '':
        pattern.append(line)
    else:
        patterns.append(pattern)
        pattern = []
patterns.append(pattern)

patterns_as_columns = []
for pattern in patterns:
    columns = []
    for row_num in range(len(pattern)):
        for column_num in range(len(pattern[row_num])):
            if row_num == 0:
                columns.append(pattern[row_num][column_num])
            else:
                columns[column_num] += pattern[row_num][column_num]
    patterns_as_columns.append(columns)

def find_symmetry_helper( pattern, index_1, index_2 ):
    if index_1 < 0:
        return True
    if index_2 >= len(pattern):
        return True

    if pattern[index_1] == pattern[index_2]:
        return find_symmetry_helper( pattern, index_1 - 1, index_2 + 1 )
    else:
        return False
    
def find_symmetry( pattern, multiplier ):
    for index in range(1,len(pattern)):
        if find_symmetry_helper( pattern, index-1, index ):
            return index*multiplier
    return 0

sum = 0

for pattern in patterns_as_columns:
    sum += find_symmetry(pattern, 1)

for pattern in patterns:
    sum += find_symmetry(pattern, 100)

print(str(sum))