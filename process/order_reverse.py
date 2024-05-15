import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import ast

with open("/Users/mrweilin/Desktop/Research/step_floor/floor_plan.json", "r") as file:
    floor_plan_content = file.read()
points = ast.literal_eval(floor_plan_content)

#reversed_data = [points[0]] + [list(reversed(sublist)) for sublist in points[1:]]
#reversed_data = [list(reversed(sublist)) for sublist in points[0:]]
reversed_data = [list(reversed(sublist)) if len(sublist) == 2 else sublist for sublist in points]


#print("points: ", reversed_data)

def coordinates_to_json(reversed_data, output_path):

    # Write to the JSON file
    with open(output_path, "w") as file:
        file.write(str(reversed_data))


coordinates_to_json(reversed_data, "./reversed_step_floor.json")