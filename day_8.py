import sys

with open(sys.argv[1]) as data:
    lines = data.readlines()
    hands = []

    linked_list = {}
    directions = None

    for line in lines:
        split_by_space = line.rstrip().split(' ')
        if split_by_space[0] == "":
            continue
        if len(split_by_space) == 1:
            directions = split_by_space[0]
        else:
            linked_list[split_by_space[0]] = { "L": split_by_space[2].removeprefix("(").removesuffix(",") , "R":split_by_space[3].removesuffix(")") }

    found = False

    count = 0
    next_node = 'AAA'
    found_zzz = False
    while not found_zzz:
        for direction in directions:
            next_node = linked_list[next_node][direction]
            if next_node == 'ZZZ':
                found_zzz = True
            count += 1

    print( "answer:" + str(count) )