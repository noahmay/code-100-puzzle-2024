import math
import json

def is_in_bar(cornerX, cornerY, width, height, x, y):
    if cornerX <= x <= cornerX + width  and cornerY <= y <= cornerY + height:
        return True
    return False

def is_in_circle(center_x, center_y, radius, x, y):
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    if distance <= radius:
        return True
    return False

def is_in_donut(center_x, center_y, outer_radius, inner_radius, x, y):
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    if outer_radius >= distance >= inner_radius:
        return True
    return False

def is_in_shapes(x, y, shapes):
    for shape in shapes:
        if shape['type'] == 'bar':
            if is_in_bar(shape['top_left_x'], shape['top_left_y'], shape['width'], shape['height'], x, y):
                return True
        elif shape['type'] == 'donut':
            if is_in_donut(shape['center_x'], shape['center_y'], shape['outer_radius'], shape['inner_radius'], x, y):
                return True
        elif shape['type'] == 'circle':
            if is_in_circle(shape['center_x'], shape['center_y'], shape['radius'], x, y):
                return True
        # Add more shapes here
    return False

 

# assignment specific code
shapes = [{
        'type': 'bar',
        'top_left_x': 145,
        'top_left_y': 75,
        'width': 20,
        'height': 150
    },
     {
        'type': 'donut',
        'center_x': 250,
        'center_y': 150,
        'outer_radius': 75,
        'inner_radius': 55
    },
     {
        'type': 'donut',
        'center_x': 410,
        'center_y': 150,
        'outer_radius': 75,
        'inner_radius': 55
    }
]
coordinates_file_path="./coordinatesystem.json"
# end of assignment specific code

file = open(coordinates_file_path)
data = json.load(file)
coordinates = data['coords']

results = [(x, y, is_in_shapes(x, y, shapes=shapes)) for (x, y) in coordinates]
# check if the last value in tuple is True
count = sum([1 for x in results if x[2]])


print(count, "points are in the black area")