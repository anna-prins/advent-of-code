import sys
import numpy as np

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

beams = np.full((len(grid[0]), len(grid)), '' )

# oof
sys.setrecursionlimit(10000)

def find_beam( grid, x, y, direction ):
    if y < 0 or y >= len(grid):
        return
    elif x < 0 or x >= len(grid[y]):
        return

    if grid[y][x] == '.':
        if direction == 'right':
            if beams[y][x] == '>':
                return
            else:
                beams[y][x] = '>'
            find_beam( grid, x+1, y, direction )
        elif direction == 'left':
            if beams[y][x] == '<':
                return
            else:
                beams[y][x] = '<'
            find_beam( grid, x-1, y, direction )
        elif direction == 'down':
            if beams[y][x] == 'v':
                return
            else:
                beams[y][x] = 'v'
            find_beam( grid, x, y+1, direction )
        else:
            if beams[y][x] == '^':
                return
            else:
                beams[y][x] = '^'
            find_beam( grid, x, y-1, direction )
    elif grid[y][x] == '\\':
        beams[y][x] = '\\'
        if direction == 'right':
            find_beam( grid, x, y+1, 'down' )
        elif direction == 'left':
            find_beam( grid, x, y-1, 'up' )
        elif direction == 'down':
            find_beam( grid, x+1, y, 'right' )
        else:
            find_beam( grid, x-1, y, 'left' )
    elif grid[y][x] == '/':
        beams[y][x] = '/'
        if direction == 'right':
            find_beam( grid, x, y-1, 'up' )
        elif direction == 'left':
            find_beam( grid, x, y+1, 'down' )
        elif direction == 'down':
            find_beam( grid, x-1, y, 'left' )
        else:
            find_beam( grid, x+1, y, 'right' )
    elif grid[y][x] == '|':
        beams[y][x] = '|'
        if direction == 'right' or direction == 'left':
            find_beam( grid, x, y-1, 'up' )
            find_beam( grid, x, y+1, 'down' )
        elif direction == 'down':
            find_beam( grid, x, y+1, direction )
        else:
            find_beam( grid, x, y-1, direction )
    elif grid[y][x] == '-':
        beams[y][x] = '-'
        if direction == 'up' or direction == 'down':
            find_beam( grid, x-1, y, 'left' )
            find_beam( grid, x+1, y, 'right' )
        elif direction == 'right':
            find_beam( grid, x+1, y, direction )
        else:
            find_beam( grid, x-1, y, direction )

find_beam(grid, 0, 0, 'right' )

print(np.count_nonzero(beams))

# part 2
energies = []

for x in range(len(grid[0])):
    biggest_y = len(grid)-1

    beams = np.full((len(grid[0]), len(grid)), '' )
    find_beam(grid, x, 0, 'down' )
    energies.append( [np.count_nonzero(beams), (x,0)] )

    beams = np.full((len(grid[0]), len(grid)), '' )
    find_beam(grid, x, biggest_y, 'up' )
    energies.append( [np.count_nonzero(beams), (x,biggest_y)] )

for y in range(1, len(grid)-1):
    biggest_x = len(grid[y])-1

    beams = np.full((len(grid[0]), len(grid)), '' )
    find_beam(grid, 0, y, 'right' )
    energies.append( [np.count_nonzero(beams), (0,y)] )

    beams = np.full((len(grid[0]), len(grid)), '' )
    find_beam(grid, biggest_x, y, 'left' )
    energies.append( [np.count_nonzero(beams), (biggest_x,y)] )

energies.sort()
print(energies[len(energies)-1])