import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import json
import math
import ast

# with open("/home/robot/Desktop/SoftRice/laser/reversed_step_floor_source.json", "r") as file:
#     floor_plan_content = file.read()
# points = ast.literal_eval(floor_plan_content)

#coordinates = [[(8.85541971311768, -33.9586226738442, 0.0), (25.086550083380402, -33.9586226738442, 0.0)], [(8.85541971311772, -33.9586226738442, 0.0), (8.503426307710281, -31.28496731706851, 0.0), (7.471433860369875, -28.7935171544327, 0.0), (5.829770950934593, -26.654060397204326, 0.0), (3.6903141937062207, -25.012397487769043, 0.0), (1.19886403107041, -23.980405040428636, 0.0), (-1.4747913257052772, -23.628411635021195, 0.0)], [(-1.47479132570528, -33.9586226738442, 0.0), (-1.47479132570528, -23.6284116350213, 0.0)], [(-20.0, -33.9586226738442, 0.0), (-1.4747913257052794, -33.9586226738442, 0.0)], [(-20.0, 0.0, 0.0), (-20.0, -33.9586226738442, 0.0)], [(-50.0, 0.0, 0.0), (-20.0, 0.0, 0.0)], [(-50.0, 7.672615941275769, 0.0), (-50.0, 0.0, 0.0)], [(-50.0, 7.672615941275801, 0.0), (-47.411809548974794, 8.013357678385116, 0.0), (-45.00000000000001, 9.01236190343141, 0.0), (-42.92893218813453, 10.601548129410318, 0.0), (-41.33974596215562, 12.672615941275788, 0.0), (-40.34074173710932, 15.084425490250577, 0.0), (-40.0, 17.67261594127578, 0.0)], [(-50.0, 17.6726159412758, 0.0), (-40.0, 17.6726159412758, 0.0)], [(-50.0, 40.0, 0.0), (-50.0, 17.6726159412758, 0.0)], [(0.0, 60.0, 0.0), (-50.00000000000001, 39.99999999999998, 0.0)], [(0.0, 76.4833844005501, 0.0), (0.0, 60.0, 0.0)], [(48.6434324787498, 76.4833844005501, 0.0), (0.0, 76.4833844005501, 0.0)], [(48.6434324787498, 65.1638435092687, 0.0), (48.6434324787498, 76.4833844005501, 0.0)], [(95.7571972694886, 65.1638435092687, 0.0), (48.6434324787498, 65.1638435092687, 0.0)], [(95.7571972694886, 58.6128336176648, 0.0), (95.7571972694886, 65.1638435092687, 0.0)], [(95.7571972694886, 58.612833617664826, 0.0), (93.41068844132239, 58.24118313019913, 0.0), (91.29387224634544, 57.16261140695642, 0.0), (89.61395740244778, 55.48269656305876, 0.0), (88.53538567920506, 53.36588036808181, 0.0), (88.16373519173938, 51.0193715399156, 0.0)], [(95.7571972694886, 51.0193715399156, 0.0), (88.1637351917394, 51.0193715399156, 0.0)], [(95.7571972694886, 40.0, 0.0), (95.7571972694886, 51.0193715399156, 0.0)], [(59.0451727572246, 40.0, 0.0), (95.7571972694886, 40.0, 0.0)], [(59.0451727572246, 14.0729427297012, 0.0), (59.0451727572246, 40.0, 0.0)], [(73.424049024528, 14.0729427297012, 0.0), (59.0451727572246, 14.0729427297012, 0.0)], [(73.424049024528, -20.0, 0.0), (73.424049024528, 14.072942729701197, 0.0)], [(44.6662964899212, -20.0, 0.0), (73.424049024528, -20.0, 0.0)], [(44.6662964899212, 0.0, 0.0), (44.6662964899212, -20.0, 0.0)], [(25.0865500833804, 0.0, 0.0), (44.6662964899212, 0.0, 0.0)], [(25.0865500833804, -33.9586226738442, 0.0), (25.0865500833804, 0.0, 0.0)], [(0.0548763623057247, 22.2616190053088, 0.0), (-28.3969426346989, 22.2616190053088, 0.0)], [(0.0548763623057269, 38.1701629606232, 0.0), (0.05487636230572468, 22.2616190053088, 0.0)], [(-28.3969426346989, 38.1701629606232, 0.0), (0.0548763623057269, 38.1701629606232, 0.0)], [(-28.3969426346989, 22.2616190053088, 0.0), (-28.3969426346989, 38.1701629606232, 0.0)], [(44.4152393146248, 8.18867627560756, 0.0), (25.4473599832884, 8.18867627560756, 0.0)], [(44.4152393146248, 10.9420781140274, 0.0), (44.4152393146248, 8.18867627560756, 0.0)], [(25.4473599832884, 10.9420781140274, 0.0), (44.4152393146248, 10.9420781140274, 0.0)], [(25.4473599832884, 8.18867627560756, 0.0), (25.4473599832884, 10.9420781140274, 0.0)], [(44.4152393146248, 2.68187259876795, 0.0), (25.4473599832884, 2.68187259876795, 0.0)], [(44.4152393146248, 5.12934089958556, 0.0), (44.4152393146248, 2.68187259876795, 0.0)], [(25.4473599832884, 5.12934089958556, 0.0), (44.4152393146248, 5.12934089958556, 0.0)], [(25.4473599832884, 2.68187259876795, 0.0), (25.4473599832884, 5.12934089958556, 0.0)], [(44.4152393146248, 70.2931844088542, 0.0), (4.643879426338728, 70.2931844088542, 0.0)], [(44.4152393146248, 72.4347191720696, 0.0), (44.4152393146248, 70.2931844088542, 0.0)], [(4.64387942633873, 72.4347191720696, 0.0), (44.4152393146248, 72.4347191720696, 0.0)], [(4.64387942633873, 70.2931844088542, 0.0), (4.64387942633873, 72.4347191720696, 0.0)], [(44.721172852227, 65.7041813448212, 0.0), (4.643879426338728, 65.7041813448212, 0.0)], [(44.721172852227, 68.241692200275, 0.0), (44.721172852227, 65.7041813448212, 0.0)], [(4.64387942633873, 68.241692200275, 0.0), (44.721172852227, 68.241692200275, 0.0)], [(4.64387942633873, 65.7041813448212, 0.0), (4.64387942633873, 68.241692200275, 0.0)]]

# compute normal vector of a plane
def compute_normal(p1, p2, p3):
    """
    Compute the normal vector of a plane defined by three points.
    """
    # Vectors v1 and v2 formed by the given points
    v1 = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
    v2 = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])

    # Compute the cross product of v1 and v2 to get the normal vector
    normal = (v1[1] * v2[2] - v1[2] * v2[1],
              v1[2] * v2[0] - v1[0] * v2[2],
              v1[0] * v2[1] - v1[1] * v2[0])

    return normal

import random

##### chooose three coordinates to calculate normal vector
def choose_coordinates(points):
    UpdatedList = random.sample(set(points), 3)
 
    print("without repetition", UpdatedList)
    return UpdatedList

# choose_coordinates(shape_coordinates)
import numpy as np

##### transform the coordinates / shape to x-y plane

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / np.sqrt(np.dot(axis, axis))
    a = np.cos(theta / 2.0)
    b, c, d = -axis * np.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([
        [aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
        [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
        [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]
    ])


### check if two vector is parallel ####

def check_parallel(A, B):
 
    # Find A.B
    per = A[0] * B[0] + A[1] * B[1] + A[2] * B[2]
 
    # Find A X B
    par = (A[1] * B[2] - A[2] * B[1]) * (A[1] * B[2] - A[2] * B[1]) + (A[0] * B[2] - B[0] * A[2]) * \
        (A[0] * B[2] - B[0] * A[2]) + (A[0] * B[1] -
                                       A[1] * B[0]) * (A[0] * B[1] - A[1] * B[0])
 
    if (per == 0):
        return 2
 
    elif (par == 0):
        return 1
 
    else:
        return 0
    
def project_to_2D(coordinates_list):
    """
    Project the 3D coordinates onto a 2D plane based on the normal vector of the shape.
    """
    
    projected_coordinates = [(x, y, segment) for x, y, _, segment in coordinates_list]  # initialization
    
    # Take any three non-collinear points from the shape to compute the normal
    coors = choose_coordinates(coordinates_list)
    normal = compute_normal(coors[0], coors[1], coors[2])
    print("normal", normal)

    target_vector = np.array([0, 0, 1])
    if (check_parallel(target_vector, normal) != 1):  ## not parallel
    
        rotation_axis = np.cross(normal, target_vector)
        
        rotation_angle = np.arccos(np.dot(normal, target_vector) / 
                                (np.linalg.norm(normal) * np.linalg.norm(target_vector)))
        R = rotation_matrix(rotation_axis, rotation_angle)

        # Rotate and project the coordinates
        rotated_coordinates = [np.dot(R, coord) for coord in coordinates_list]
        projected_coordinates = [(x, y, segment) for x, y, _, segment in rotated_coordinates]

# Load the output JSON to a Python object
# with open("./reverse_step_floor.json", "r") as file:
#     data = json.load(file)

# # Add the segment attribute to each point based on the index of the segment
# for index, segment in enumerate(data):
#     for point in segment['points']:
#         point['segment'] = index

# # Save the modified data back to the JSON file
# output_file_path = "./reverse_step_floor.json"
# with open(output_file_path, "w") as modified_output_file:
#     json.dump(data, modified_output_file, indent=4)

    return projected_coordinates

def interpolate_points(points, count, spacing=1.0):
    """Interpolates between given points with a consistent spacing.
    
    If the input list contains only two points, it linearly interpolates between them.
    If the input list contains more than two points, it uses B-spline interpolation.
    """
    
    def euclidean_distance(p1, p2):
        return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    
    if len(points) == 2:
        total_length = euclidean_distance(points[0], points[1])
        num_points = int(total_length / spacing) + 1
        t_values = np.linspace(0, 1, num_points)

        x_interpolated = np.interp(t_values, [0, 1], [points[0][0], points[1][0]])
        y_interpolated = np.interp(t_values, [0, 1], [points[0][1], points[1][1]])
        z_interpolated = np.interp(t_values, [0, 1], [points[0][2], points[1][2]])
        
    else:
        x_vals = [point[0] for point in points]
        y_vals = [point[1] for point in points]
        z_vals = [point[2] for point in points]
        
        tck, u = splprep([x_vals, y_vals, z_vals], s=0)
        
        # Compute the total length of the spline
        u_fine = np.linspace(0, 1, len(points) * 10)  # a fine sampling
        spline_points_fine = np.array(splev(u_fine, tck))
        total_length = np.sum(np.sqrt(np.sum(np.diff(spline_points_fine, axis=1)**2, axis=0)))
        
        num_points = int(total_length / spacing) + 1
        u_new = np.linspace(0, 1, num_points)
        x_interpolated, y_interpolated, z_interpolated = splev(u_new, tck)

    num_segments_points = [count]  * num_points

    return list(zip(x_interpolated, y_interpolated, z_interpolated, num_segments_points))


############# Upscale to the ilda coordinate system #####################

def upscale(coordinates, new_min=-30000, new_max=30000):
    x, y, segment = zip(*coordinates)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)


    new_list = []

    for i in coordinates:
        # Handling the case where x_max = x_min to avoid division by zero
        if x_max == x_min:
            xx = (new_max + new_min) // 2  # centering the point in the new range
        else:
            xx = ((i[0] - x_min) / (x_max - x_min)) * (new_max - new_min) + new_min

        # Handling the case where y_max = y_min to avoid division by zero
        if y_max == y_min:
            yy = (new_max + new_min) // 2  # centering the point in the new range
        else:
            yy = ((i[1] - y_min) / (y_max - y_min)) * (new_max - new_min) + new_min

        
        

        temp = (xx, yy,i[2])
        new_list.append(temp)  # store the processed coordinates

    return new_list



############## scale the coordinate to (-1,1) #####################

# def upscale(coordinates, new_min=-1, new_max=1):
#     x, y = zip(*coordinates)
#     x_min = min(x)
#     x_max = max(x)
#     y_min = min(y)
#     y_max = max(y)

#     new_list = []counter

#     for i in coordinates:
#         # Handling the case where x_max = x_min to avoid division by zero
#         if x_max == x_min:
#             xx = (new_max + new_min) / 2  # centering the point in the new range
#         else:
#             xx = ((i[0] - x_min) / (x_max - x_min)) * (new_max - new_min) + new_min

#         # Handling the case where y_max = y_min to avoid division by zero
#         if y_max == y_min:
#             yy = (new_max + new_min) / 2  # centering the point in the new range
#         else:
#             yy = ((i[1] - y_min) / (y_max - y_min)) * (new_max - new_min) + new_min
        
#         temp = (xx, yy)
#         new_list.append(temp)  # store the processed coordinates

#     return new_list


def coordinates_to_json(coordinates, output_path):

    # Convert to the JSON format
    points_list = [{
        # 'x': int(x),  ### the original (-30000, 30000)
        # 'y': int(y), ### the original (-30000, 30000)\
        'segment': segment,
        'x': x, ## for (-1,1)
        'y': y, ## for (-1,1)
        # 'z': 0,
        'color': 0,  # Default based on example
        'blanking': False  # Default based on example
    } for x, y, segment in coordinates]

    template = {
        'type': 1,
        'name': '',
        'company': '',
        'index': 0,
        'points': points_list,
        'head': 0,
        'total': 1,
        'colors': []
    }
    header = {
        "name": "END OF F", 
        "type": 1,
        "points": [],
        "colors": [],
        "company": "FILE",
        "total": 1,
        "head": 0
    }

    # Write to the JSON file
    with open(output_path, "w") as file:
        json.dump([template, header], file)


# points = ast.literal_eval(coordinates)

# count = 0
# interpolated_coordinates = []
# for segment in points:
#     interpolated_coordinates.extend(interpolate_points(segment, count))
#     count +=1

# print("interpolated_coordinates ", interpolated_coordinates)

# new_shape_coordinates = project_to_2D(interpolated_coordinates)

# print("new_shape_coordinates", new_shape_coordinates)

# upscaled_coordinates = upscale(new_shape_coordinates)

# print("upscaled points", upscaled_coordinates)

# Plotting the interpolated coordinates in 2D
# x_coords = [point[0] for point in upscaled_coordinates]
# y_coords = [point[1] for point in upscaled_coordinates]

# plt.figure(figsize=(10, 7))
# plt.scatter(x_coords, y_coords, c='blue', marker='o')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Interpolated Coordinates in 2D Space')
# plt.grid(True)
# plt.axis('equal')
# plt.show()


############### write the extracted coordiantes to json fiile ############


# coordinates_to_json(upscaled_coordinates, "./reverse_step_floor.json")
