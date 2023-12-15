import sys
import numpy as np
import math

with open(sys.argv[1]) as data:
    file = data.read()
lines = file.split('\n')

list_of_lists = []

for line in lines:
    split_line = []
    for char in range(len(line)):
        split_line.append(line[char])
    list_of_lists.append(split_line)

grid = np.array(list_of_lists)

# ahhhhhh
def bubble_sort(column):
    made_switch = False
    for row in range(1, len(column)):
        prev_row = row-1
        if column[row] == 'O' and column[prev_row] == '.':
            column[row] = '.'
            column[prev_row] = 'O'
            made_switch = True
    if made_switch:
        return bubble_sort(column)
    else:
        return column

def tilt(grid):
    for column in range(len(grid[0])):
        grid[:,column] = bubble_sort(grid[:,column])

def cycle(grid):
    tilt(grid)

    for _ in range(3):
        grid = np.rot90(grid, 3)
        tilt(grid)

desired_cycle_amount = 1000000000
cycles = []

def find_loop(grid, cycle_number):
    cycle(grid)
    cycle_number += 1
    flattened_grid = grid.flatten().tolist()
    if flattened_grid in cycles:
        return (cycles.index(flattened_grid)+1, cycle_number)
    cycles.append(flattened_grid)
    return find_loop(grid, cycle_number)

start_loop, end_loop = find_loop(grid, 0)

loop_length = end_loop-start_loop
remaining_cycles = desired_cycle_amount - start_loop
full_cycles = math.floor(remaining_cycles/loop_length)
remaining_cycles = remaining_cycles-(full_cycles*loop_length)

for _ in range(0,remaining_cycles):
    cycle(grid)

def calculate_load(grid):
    flipped_grid = np.flip(grid, 0)
    load = 0
    for x in range(len(grid[0])):
        for y in range(len(grid[:,0])):
            thing = flipped_grid[x][y]
            if thing == 'O':
                load += x + 1
    return load

print(calculate_load(grid))