import sys

with open(sys.argv[1]) as data:
    lines = data.readlines()
    seeds = lines[0].removeprefix("seeds: ").rstrip().split(" ")

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

    for seed in seeds:
        soil, fertilizer, water, light, temp, humidity, location = None, None, None, None, None, None, None

        converted = False
        for conversion in seed_to_soil:
            int_seed = int(seed)
            if int_seed >= conversion['source'] and int_seed < ( conversion['source'] + conversion['range'] ):
                soil = int_seed - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            soil = int_seed

        converted = False
        for conversion in soil_to_fertilizer:
            if soil >= conversion['source'] and soil < ( conversion['source'] + conversion['range'] ):
                fertilizer = soil - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            fertilizer = soil

        converted = False
        for conversion in fertilizer_to_water:
            if fertilizer >= conversion['source'] and fertilizer < ( conversion['source'] + conversion['range'] ):
                water = fertilizer - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            water = fertilizer

        converted = False
        for conversion in water_to_light:
            if water >= conversion['source'] and water < ( conversion['source'] + conversion['range'] ):
                light = water - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            light = water

        converted = False
        for conversion in light_to_temp:
            if light >= conversion['source'] and light < ( conversion['source'] + conversion['range'] ):
                temp = light - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            temp = light

        converted = False
        for conversion in temp_to_humidity:
            if temp >= conversion['source'] and temp < ( conversion['source'] + conversion['range'] ):
                humidity = temp - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            humidity = temp

        converted = False
        for conversion in humidity_to_location:
            if humidity >= conversion['source'] and humidity < ( conversion['source'] + conversion['range'] ):
                location = humidity - conversion['source'] + conversion['dest']
                converted = True
        if not converted:    
            location = humidity

        if lowest_location is None:
            lowest_location = location
        elif location < lowest_location:
            lowest_location = location

    print( "lowest location: " + str(lowest_location) )