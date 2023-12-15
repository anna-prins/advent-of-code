import sys

with open(sys.argv[1]) as data:
    file = data.readline()

steps = file.strip().split(',')

hash_sum = 0
for step in steps:
    hash = 0
    for char in step:
        hash = ((hash + ord(char))*17)%256
    hash_sum += hash

print(hash_sum)