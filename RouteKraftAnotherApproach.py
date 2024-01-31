import cv2
import numpy as np
from random import randint
from scipy.spatial.distance import euclidean

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

climber_height = int(input("Enter your height in cms : "))

first_hold_x = wall_width // 2

first_hold_y = randint(climber_height // 2, climber_height)

first_hold_y = wall_height - first_hold_y

first_hold = [first_hold_x, first_hold_y]

print(f"First Hold Coordinates : {first_hold}")

cv2.circle(wall_img, tuple(first_hold), 4, (0, 0, 255), -1)

second_hold_x = randint(first_hold_x - 50, first_hold_x + 50)

second_hold_y = randint(first_hold_y + 30, first_hold_y + 50)

second_hold = [second_hold_x, second_hold_y]

print(f"Second Hold Coordinates : {second_hold}")

cv2.circle(wall_img, tuple(second_hold), 4, (0, 0, 255), -1)

third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)

third_hold_y = randint(second_hold_y + 30, second_hold_y + 50)

third_hold = [third_hold_x, third_hold_y]

distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))

distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))

while distance_between_first_and_third + 20 < distance_between_second_and_third:
    third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)
    third_hold_y = randint(second_hold_y + 30, second_hold_y + 50)
    third_hold = [third_hold_x, third_hold_y]
    distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))
    distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))

print(f"Third Hold Coordinates : {third_hold}")

print(f"The distance between first & third hold is {distance_between_first_and_third}")

print(f"The distance between second & third hold is {distance_between_second_and_third}")

cv2.circle(wall_img, tuple(third_hold), 4, (0, 0, 255), -1)

cv2.imshow("RouteKraft", wall_img)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()



