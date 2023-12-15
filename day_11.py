import sys
import itertools

with open(sys.argv[1]) as data:
    file = data.read()
rows = file.split('\n')

columns = []

for row_num in range(len(rows)):
    for column_num in range(len(rows[row_num])):
        if row_num == 0:
            columns.append(rows[row_num][column_num])
        else:
            columns[column_num] += rows[row_num][column_num]

empty_cols = []
for col_num in range(len(columns)):
    if columns[col_num].find('#') == -1:
        empty_cols.append(col_num)

empty_rows = []
for row_num in range(len(rows)):
    if rows[row_num].find('#') == -1:
        empty_rows.append(row_num)

numbers = []
count = 1
for row_num in range(len(rows)):
    for col in range(len(rows[row_num])):
        if rows[row_num][col] == '#':
            count += 1
            numbers.append((col, row_num ))

combinations_list = list(itertools.combinations(range(len(numbers)), 2))

sum_of_distances = 0

for combo in combinations_list:
    ax = numbers[combo[0]][0]
    ay = numbers[combo[0]][1]

    bx = numbers[combo[1]][0]
    by = numbers[combo[1]][1]

    def add_padding( empty_spaces, first, second ):
        padding = 0
        for empty_space in empty_spaces:
            if (first <= empty_space and second >= empty_space) or (second <= empty_space and first >= empty_space):
                padding += 1
        return padding
    
    x_distance = 0
    if bx >= ax:
        x_distance = bx - ax
        x_distance += add_padding( empty_cols, ax, bx )
    else:
        x_distance = ax - bx
        x_distance += add_padding( empty_cols, bx, ax )

    y_distance = 0
    if by >= ay:
        y_distance = by - ay
        y_distance += add_padding( empty_rows, ay, by )
    else:
        y_distance = ay - by
        y_distance += add_padding( empty_rows, by, ay )

    distance = x_distance + y_distance
    sum_of_distances += distance

print(sum_of_distances)