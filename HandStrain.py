import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def apply_field(global_field_x, global_field_y, global_x, global_y, field_values, c_field):
    """Given a polygon (c_field) and desired values, adds to strain field in this polygon"""
    polygon = Polygon(c_field)

    for i in range(len(global_x)):
        for j in range(len(global_x[0])):
            point = Point(global_x[i][j], global_y[i][j])
            if polygon.contains(point):
                global_field_x[i][j] += field_values[0]
                global_field_y[i][j] += field_values[1]

    return [global_field_x, global_field_y]


def get_hand_field(palm=(0, 0), thumb1=(0, 0), thumb2=(0, 0), index1=(0, 0), index2=(0, 0),
                   middle1=(0, 0), middle2=(0, 0), ring1=(0, 0), ring2=(0, 0), pinky1=(0, 0), pinky2=(0, 0)):

    x, y = np.meshgrid(np.linspace(1, 200, 200), np.linspace(1, 200, 200))

    u = x*0
    v = y*0

    # Coordinates of polygons in the inkscape drawing
    c_palm = [[72.76, 76.94], [162.26, 76.80], [161.93, 104.11], [72.53, 104.01]]
    c_thumb1 = [[54.91, 69.74], [72.64, 76.85], [51.31, 103.51], [33.35, 96.40]]
    c_thumb2 = [[28.76, 94.76], [48.08, 102.38], [44.62, 117.49], [25.12, 109.77]]
    c_index1 = [[72.56, 104.05], [92.08, 104.25], [87.11, 144.20], [67.47, 144.26]]
    c_index2 = [[70.11, 144.40], [86.19, 144.26], [81.23, 183.62], [64.89, 183.75]]
    c_middle1 = [[98.69, 104.11], [116.75, 103.98], [118.14, 150.88], [99.75, 150.75]]
    c_middle2 = [[100.08, 151.14], [118.47, 151.28], [118.33, 187.92], [100.34, 187.92]]
    c_ring1 = [[123.49, 104.38], [139.17, 104.25], [146.31, 149.36], [130.84, 149.23]]
    c_ring2 = [[131.63, 148.89], [145.19, 148.89], [150.88, 180.25], [137.05, 180.45]]
    c_pinky1 = [[145.74, 104.16], [162.21, 104.35], [172.50, 134.61], [156.31, 134.75]]
    c_pinky2 = [[156.59, 134.56], [169.74, 134.52], [177.50, 157.11], [164.40, 157.25]]

    # Apply strain to every polygon in turn
    output_field = apply_field(u, v, x, y, palm, c_palm)
    output_field = apply_field(output_field[0], output_field[1], x, y, thumb1, c_thumb1)
    output_field = apply_field(output_field[0], output_field[1], x, y, thumb2, c_thumb2)
    output_field = apply_field(output_field[0], output_field[1], x, y, index1, c_index1)
    output_field = apply_field(output_field[0], output_field[1], x, y, index2, c_index2)
    output_field = apply_field(output_field[0], output_field[1], x, y, middle1, c_middle1)
    output_field = apply_field(output_field[0], output_field[1], x, y, middle2, c_middle2)
    output_field = apply_field(output_field[0], output_field[1], x, y, ring1, c_ring1)
    output_field = apply_field(output_field[0], output_field[1], x, y, ring2, c_ring2)
    output_field = apply_field(output_field[0], output_field[1], x, y, pinky1, c_pinky1)
    output_field = apply_field(output_field[0], output_field[1], x, y, pinky2, c_pinky2)

    return output_field
