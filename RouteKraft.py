import cv2
import numpy as np
# import os
from itertools import product
from scipy.spatial.distance import euclidean
import random

""" def convert_to_cms(value, unit):
    if unit.lower() == 'meters':
        return value * 100
    elif unit.lower() == 'feet':
        return value * 30.48
    elif unit.lower() == 'inches':
        return value * 2.54
    else:
        return value

def get_input_in_cms(wall_width, wall_height, unit):
    width_cm = convert_to_cms(wall_width, unit)
    while width_cm < 200:
        width = int(input("Enter a higher value for wall's width : "))
        width_cm = convert_to_cms(width, unit)
        if width_cm < 200:
            print("Please enter a value equal to or more than 200 cms.")

    height_cm = convert_to_cms(wall_height, unit)
    while height_cm < 200:
        height = int(input("Enter a higher value for wall's height : "))
        height_cm = convert_to_cms(height, unit)
        if height_cm < 200:
            print("Please enter a value equal to or more than 200 cms.")
    return width_cm, height_cm


unit = input("Enter the unit for width and height (e.g., meters, feet, inches, cms): ")
wall_width = int(input(f"Enter the value for width in {unit}"))
wall_height = int(input(f"Enter the value for height in {unit}"))

wall_width_cms, wall_height_cms = get_input_in_cms(wall_width, wall_height, unit)

print(f"Wall Width in cms: {wall_width}")
print(f"Wall Height in cms: {wall_height}") """


wall_width = int(input("Enter the climbing wall's width in cms : "))

# Minimum wall width = 200 cms
while wall_width < 200: 
    wall_width = int(input("Kindly input a value equal to 200 or more in cms (200 cms = 80 inches = 6.66 Feet) for Width of the Wall : "))

wall_height = int(input("Enter the climbing wall's height in cms : "))

# Minimum wall height = 200 cms
while wall_height < 200: 
    wall_width = int(input("Kindly input a value equal to 200 or more in cms (200 cms = 80 inches = 6.66 Feet) for Height of the Wall : "))

# Creating the wall image
wall_img = np.full((wall_width, wall_height, 3), fill_value=127, dtype = np.uint8)

# Creating a copy of the wall image
wall_img_random_num_centres = wall_img.copy()

img_height_px, img_width_px, img_channels = wall_img.shape

# print("Image Height In Pixels : ", img_height_px)
# print("Image Width In Pixels : ", img_width_px)
# print("No. Of Channels in the Image : ", img_channels)

# Length of side of a squared cell in the grid that is being drawn on the wall
cell_side = 100 # in centimetres, this would be the length in pixels too # 100 cm = 1 m = 3.5 Ft

# Drawing the Grid
# Draw horizontal lines
for y in range(0, wall_height, cell_side):
    cv2.line(wall_img, (0, y), (wall_width, y), (0, 0, 255), 2)
    cv2.line(wall_img_random_num_centres, (0, y), (wall_width, y), (0, 0, 255), 2)

# Draw vertical lines
for x in range(0, wall_width, cell_side):
    cv2.line(wall_img, (x, 0), (x, wall_height), (255, 0, 0), 2)
    cv2.line(wall_img_random_num_centres, (x, 0), (x, wall_height), (255, 0, 0), 2)

# Calculate total number of cells
total_cells = (img_width_px // cell_side) * (img_height_px // cell_side)
print("Total Number of Cells in the Grid:", total_cells)
total_possible_positions_for_holds = total_cells

# Choose a random number of centers to draw points for
num_centers_to_draw = random.randint(1, total_cells)

# Draw points at the center of each cell and label with coordinates
centers = []
for row, y in enumerate(range(0, wall_height, cell_side)):
    for col, x in enumerate(range(0, wall_width, cell_side)):
        cell_center = (x + cell_side // 2, y + cell_side // 2)
        centers.append((cell_center, (col, row)))

        # Draw point
        cv2.circle(wall_img, cell_center, 3, (0, 255, 0), -1)

        # Write coordinates beside the point
        text = f"({x + cell_side // 2}, {y + cell_side // 2})"
        # print(f"Center of Cell at row {row}, column {col}:", cell_center)
        # print("Center of Cell at (", x, ",", y, "):", cell_center)
        cv2.putText(wall_img, text, (x + cell_side // 2 + 5, y + cell_side // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        # + 5: This is an additional offset added to the x-coordinate. It moves the text 5 pixels to the right of the center. The purpose of this offset is to visually separate the text from the center point, making it easier to read. 
        

# Shuffle the list of centers randomly
random.shuffle(centers)

# Randomly choose the number of cells to draw centers for
num_cells_to_draw = random.randint(8, total_cells - total_cells // 2)

# Draw points at the center of randomly chosen cells
for center, (col, row) in centers[:num_cells_to_draw]:
    cv2.circle(wall_img_random_num_centres, center, 3, (0, 255, 0), -1)
    text = f"({col * cell_side + cell_side // 2}, {row * cell_side + cell_side // 2})"
    cv2.putText(wall_img_random_num_centres, text, (center[0] + 5, center[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

# Calculate and store distances between centers
distances = []
for (i, (center1, coord1)), (j, (center2, coord2)) in product(enumerate(centers), repeat=2):
    if i != j:
        distance = euclidean(center1, center2)
        distances.append({
            'centers': (coord1, coord2),
            'distance': distance
        })

# The product function from the itertools module is used to iterate over all pairs of centers. The enumerate(centers) ensures that you get both the index i and the actual center information (center1, coord1) in the loop.

# enumerate(centers): The enumerate function is used to iterate over the centers list, providing both the index i and the actual center point center1. This gives pairs of (i, center1).

# product(..., repeat=2): The product function from the itertools module is used to compute the Cartesian product of the enumerated centers with itself (repeat=2). This results in pairs of pairs, or in other words, all combinations of two distinct centers.

# for (i, center1), (j, center2) in ...: The outer loop iterates over all pairs of centers, providing two pairs of (i, center1) and (j, center2).

# if i != j:: This condition ensures that the distance between a center and itself is not calculated (i.e., center1 is not the same as center2).

# distance = euclidean(center1, center2): The euclidean function from the scipy.spatial.distance module calculates the Euclidean distance between center1 and center2.

# Access the distances between the centres of the cells 
for entry in distances:
    coord1, coord2 = entry['centers']
    distance = entry['distance']
    print(f"Distance between centers {coord1} and {coord2}: {distance}")

# print(f"Distance between centers {i} and {j}: {distance}"): Finally, the code prints the distance between the centers along with their indices. The f-string is used for formatting the output.
    
# print(len(centers))

# Displaying the Wall Image with the Grid
cv2.imshow("Indoor Climbing Wall", wall_img)

# Displaying the Wall Image with the Grid
cv2.imshow("Indoor Climbing Wall With Random Number Of Centres", wall_img_random_num_centres)

k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()

