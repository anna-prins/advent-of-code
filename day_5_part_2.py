import sys

with open(sys.argv[1]) as data:
    lines = data.readlines()
    seed_line = lines[0].removeprefix("seeds: ").rstrip().split(" ")

    number = 0
    seeds = []
    while number < len(seed_line):
        info = {}
        info['start'] = int(seed_line[number])
        info['length'] = int(seed_line[number+1])
        seeds.append(info)
        number += 2

    def read_next_map( list, i ):
        i += 2
        current_line = lines[i]
        while current_line != '\n':
            map = {}
            info = current_line.rstrip().split(" ")
            map['source'] = int(info[1])
            map['dest'] = int(info[0])
            map['range'] = int(info[2])
            list.append(map)
            i += 1
            if i < len(lines):
                current_line = lines[i]
            else:
                break
        return i

    index = 1
    seed_to_soil = []
    index = read_next_map( seed_to_soil, index )

    soil_to_fertilizer = []
    index = read_next_map( soil_to_fertilizer, index )

    fertilizer_to_water = []
    index = read_next_map( fertilizer_to_water, index )

    water_to_light = []
    index = read_next_map( water_to_light, index )

    light_to_temp = []
    index = read_next_map( light_to_temp, index )

    temp_to_humidity = []
    index = read_next_map( temp_to_humidity, index )

    humidity_to_location = []
    index = read_next_map( humidity_to_location, index )

    lowest_location = None

    soil, fertilizer, water, light, temp, humidity, seed = None, None, None, None, None, None, None

    achieved_conversion = False
    location = 0
    while not achieved_conversion:
        def convert( source, destination, map ):
            converted = False
            for conversion in map:
                if destination >= conversion['dest'] and destination < ( conversion['dest'] + conversion['range'] ):
                    source = destination - conversion['dest'] + conversion['source']
                    converted = True
            if not converted:
                source = destination
            return source

        humidity = convert( humidity, location, humidity_to_location )
        temp = convert ( temp, humidity, temp_to_humidity )
        light = convert( light, temp, light_to_temp )
        water = convert( water, light, water_to_light )
        fertilizer = convert( fertilizer, water, fertilizer_to_water )
        soil = convert( soil, fertilizer, soil_to_fertilizer )
        seed = convert( seed, soil, seed_to_soil )

        for seed_pack in seeds:
            if seed >= seed_pack['start'] and seed < seed_pack['start'] + seed_pack['length']:
                print('found seed: ' + str(seed) + " at location " + str(location))
                achieved_conversion = True

        location += 1
