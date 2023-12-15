import sys

with open(sys.argv[1]) as data:
    file = data.read()
lines = file.split('\n')

columns = []

for row_num in range(len(lines)):
    for column_num in range(len(lines[row_num])):
        if row_num == 0:
            columns.append(lines[row_num][column_num])
        else:
            columns[column_num] += lines[row_num][column_num]

for column in range(len(columns)):
    columns[column] = columns[column][::-1]

load = 0

for column in range(len(columns)):
    num_Os = 0
    final_column = ''
    for index in range(len(columns[column])):
        if columns[column][index] == '#':
            if num_Os != 0:
                final_column = final_column[:index-num_Os] + ('O'*num_Os)
                num_Os = 0
            final_column += '#'
        elif columns[column][index] == 'O':
            final_column += '.'
            num_Os += 1
        else:
            final_column += '.'
    if num_Os != 0:
        final_column = final_column[:-num_Os] + ('O'*num_Os)
    columns[column] = final_column

    for index in range(len(columns[column])):
        if columns[column][index] == 'O':
            load += index + 1

print(load)