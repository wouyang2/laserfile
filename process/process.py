import Path2
#import order_reverse
import plot_segment
import ast
import json
import matplotlib.pyplot as plt


def process(input_file, output_file):
    
    #ORDER_REVERSE
    with open(input_file, "r") as file:
        floor_plan_content = file.read()
        points = ast.literal_eval(floor_plan_content)

    reversed_data = [list(reversed(sublist)) if len(sublist) == 2 else sublist for sublist in points]

    with open(output_file, "w") as file:
        file.write(str(reversed_data))



    #PLOT_SEGMENT
    with open(output_file, "r") as file:
        floor_plan_content = file.read()
        points = ast.literal_eval(floor_plan_content)

    count = 0
    interpolated_coordinates = []
    for segment in points:
        interpolated_coordinates.extend(plot_segment.interpolate_points(segment, count))
        count +=1

    new_shape_coordinates = plot_segment.project_to_2D(interpolated_coordinates)

    upscaled_coordinates = plot_segment.upscale(new_shape_coordinates)
    #Plotting the interpolated coordinates in 2D
    x_coords = [point[0] for point in upscaled_coordinates]
    y_coords = [point[1] for point in upscaled_coordinates]

    plt.figure(figsize=(10, 7))
    plt.scatter(x_coords, y_coords, c='blue', marker='o')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Interpolated Coordinates in 2D Space')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

    plot_segment.coordinates_to_json(upscaled_coordinates, output_file)


    #PATH2

    with open(output_file, "r") as file:
        data = json.load(file)

    modified_points = Path2.insert_interpolated_points(data[0]['points'])
    data[0]['points'] = modified_points

    with open(output_file, "w") as file:
        json.dump(data, file)


process("/Users/mrweilin/Desktop/Research/New_floor/revise_new_floor.json", "/Users/mrweilin/Desktop/Research/New_floor/final_new_floor.json")