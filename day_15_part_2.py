import sys

with open(sys.argv[1]) as data:
    file = data.readline()

steps = file.strip().split(',')

boxes = [[] for _ in range(256)]

def hash(string, current_value):
    if string == '':
        return current_value
    return hash(string[1:], ((current_value + ord(string[0]))*17)%256)
        
for step in steps:
    if '=' in step:
        new_lens = step.split('=')
        box_number = hash(new_lens[0], 0)
        found_matching_label = False
        for lens in range(len(boxes[box_number])):
            if boxes[box_number][lens][0] == new_lens[0]:
                boxes[box_number][lens][1] = new_lens[1]
                found_matching_label = True
                break
        if not found_matching_label:
            boxes[box_number].append(new_lens)
    else:
        label = step[:-1]
        box_number = hash(label, 0)
        for lens in range(len(boxes[box_number])):
            if boxes[box_number][lens][0] == label:
                boxes[box_number].pop(lens)
                break

focusing_power = 0
for box in range(len(boxes)):
    if len(boxes[box]) != 0:
        for lens in range(len(boxes[box])):
            focusing_power += (1 + box)*(1+lens)*int(boxes[box][lens][1])

print(focusing_power)