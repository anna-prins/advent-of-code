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

def find_smudges_helper( pattern, index_1, index_2, smudges ):
    if index_1 < 0:
        return smudges
    if index_2 >= len(pattern):
        return smudges

    if pattern[index_1] != pattern[index_2]:
        for index in range(len(pattern[index_1])):
            if pattern[index_1][index] != pattern[index_2][index]:
                smudges += 1
    return find_smudges_helper( pattern, index_1 - 1, index_2 + 1, smudges )
    
def find_symmetry( pattern, multiplier ):
    for index in range(1,len(pattern)):
        if find_smudges_helper( pattern, index-1, index, 0 ) == 1:
            return index*multiplier
    return 0

sum = 0

for vertical, horizontal in zip(patterns_as_columns, patterns):
    vertical_symmetry = find_symmetry( vertical, 1 )
    horizontal_symmetry = find_symmetry( horizontal, 100 )

    sum += horizontal_symmetry + vertical_symmetry

print(str(sum))