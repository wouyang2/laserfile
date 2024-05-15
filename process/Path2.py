import json

def interpolate_points(start, end, distance=1000):
    """
    Generate interpolated points between start and end points with specified distance.
    
    Args:
    - start (tuple): Starting point as (x, y).
    - end (tuple): Ending point as (x, y).
    - distance (int): Distance between interpolated points.

    Returns:
    - List of interpolated points including start and end.
    """
    x1, y1 = start
    x2, y2 = end
    points = [start]

    # Calculate total distance and direction
    total_distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    # If total_distance is zero, return just the start and end points
    if total_distance == 0:
        return [start, end]
    
    x_dir = (x2 - x1) / total_distance
    y_dir = (y2 - y1) / total_distance

    num_points = int(total_distance / distance)
    for i in range(1, num_points):
        new_x = x1 + i * distance * x_dir
        new_y = y1 + i * distance * y_dir
        points.append((new_x, new_y))

    points.append(end)
    return points

def insert_interpolated_points(data):
    """Insert interpolated points between two points with different segment values."""
    new_data = []
    
    # Copy the very first point, set it to true, and place it at the beginning
    # first_point = data[0].copy()
    # first_point['blanking'] = True
    # new_data.append(first_point)
    
    for i in range(len(data) - 1):
        # Append the current point to the new data
        new_data.append(data[i])
        
        # If the segment of the current point is different from the next point's segment
        if data[i]['segment'] != data[i + 1]['segment']:

            for _ in range(2):
                new_data.append(data[i].copy())

            # Get interpolated points
            interpolated = interpolate_points(
                (data[i]['x'], data[i]['y']),
                (data[i + 1]['x'], data[i + 1]['y'])
            )
            
            # Convert interpolated points to the format in the JSON data
            # for point in interpolated:  # Including start and end points
            #     new_data.append({
            #         'x': point[0],
            #         'y': point[1],
            #         'color': data[i]['color'],  # Using the current color
            #         'blanking': True  # Setting blanking to True for all interpolated points
            #     })

            for point in interpolated[1:]:  # Excluding the interpolated starting point
                new_data.append({
                    'x': point[0],
                    'y': point[1],
                    'color': data[0]['color'],  # Using the color of the first point
                    'blanking': True  # Setting blanking to True for all interpolated points
                })
                
    # Append the original last point
    new_data.append(data[-1])
    
    # Copy the last point, set it to true, and place it at the end
    last_point = data[-1].copy()
    last_point['blanking'] = True
    new_data.append(last_point)
    
    # Interpolate between the first and last points and insert them at the end
    interpolated_start_end = interpolate_points(
        (data[-1]['x'], data[-1]['y']),
        (data[0]['x'], data[0]['y'])
    )
    for point in interpolated_start_end:
        new_data.append({
            'x': point[0],
            'y': point[1],
            'color': data[-1]['color'],  # Using the color of the last point
            'blanking': True  # Setting blanking to True for all interpolated points
        })

    # Copy the very first point, set it to true, and place it at the end
    first_point = data[0].copy()
    first_point['blanking'] = True
    new_data.append(first_point)

    return new_data



# Load the json file content
#with open("/home/robot/Desktop/SoftRice/laser/new_floor/reversed_new_floor.json", "r") as file:
    #data = json.load(file)

# Apply the interpolation and insertion
#modified_points = insert_interpolated_points(data[0]['points'])
#data[0]['points'] = modified_points


# (Optional) Save the modified data to a new JSON file
#with open("/home/robot/Desktop/SoftRice/laser/new_floor/final_new_floor.json", "w") as file:
    #json.dump(data, file)
