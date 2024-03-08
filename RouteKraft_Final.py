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
wall_img = np.full((wall_width, wall_height, 3), fill_value=255, dtype = np.uint8)

# Images of Holds

# width & height of the hold image

crimp_width, crimp_height = 16, 16
crimp = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\crimp.png"), (crimp_width, crimp_height))

pinch_width, pinch_height = 10, 26
pinch = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\pinch.png"), (pinch_width, pinch_height))

edge_width, edge_height = 20, 16
edge = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\edge.png"), (edge_width, edge_height))

pocket_width, pocket_height = 26, 26
pocket = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\pocket.png"), (pocket_width, pocket_height))

jug_width, jug_height = 30, 30
jug = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\jug.png"), (jug_width, jug_height))

sloper_width, sloper_height = 40, 40
sloper = cv2.resize(cv2.imread(".\\rockclimbingholdsimages\\sloper.png"), (sloper_width, sloper_height))

holds_list = [[crimp, [crimp_width, crimp_height], "Crimp"], [pinch, [pinch_width, pinch_height], "Pinch"], [edge, [edge_width, edge_height], "Edge"], [pocket, [pocket_width, pocket_height], "Pocket"], [jug, [jug_width, jug_height], "Jug"], [sloper, [sloper_width, sloper_height], "Sloper"]]

# Climber's height

climber_height = int(input("Enter your height in cms : "))

# 2 feet = 60.96 centimeters (minimum height)
# 10 feet = 304.8 centimeters (maximum height)

while climber_height < 60 or climber_height > 305:
        climber_height = int(input("Enter a value greater than 60 cms and less than 305 cms for your height : "))


# Values being subtracted from y coordinates for every hold to find the y coordinate of the next hold should also be according to the climber's height and experience in climbing
        
# we need to put images for holds on the coordinates figured out for all the holds

# difficulty of routes should be taken as easy, medium & hard based on the climber's experience
        
# more routes should be provided on the wall following a similar approach

# Position of First hold
    
first_hold_x = wall_width // 2

first_hold_y = randint(climber_height // 2, climber_height)

first_hold_y = wall_height - first_hold_y 

first_hold = [first_hold_x, first_hold_y]

first_hold_y_show = wall_height - first_hold_y

# Placing first hold image on the wall image

# Finding a random hold from the holds_list for the first hold

hold_ind = randint(0, len(holds_list) - 1)

first_hold_list = holds_list[hold_ind]
first_hold_image = holds_list[hold_ind][0]
first_hold_name = holds_list[hold_ind][2]

first_hold_width = first_hold_list[1][0]
first_hold_height = first_hold_list[1][1]

value_for_x = first_hold_width // 2
value_for_y = first_hold_height // 2
     
# top left corner x & y coordinates for the image of first hold

first_hold_img_tl_x = first_hold_x - value_for_x
first_hold_img_tl_y = first_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of first hold

first_hold_img_br_x = first_hold_x + value_for_x
first_hold_img_br_y = first_hold_y + value_for_y

# print(f"First Hold Image Coords : {first_hold_img_tl_x, first_hold_img_tl_y}, {first_hold_img_br_x, first_hold_img_br_y}")

wall_img[first_hold_img_tl_y : first_hold_img_br_y, first_hold_img_tl_x : first_hold_img_br_x] = first_hold_image

print(f"First Hold Name : {first_hold_name} & First Hold Coordinates : ({first_hold_x}, {first_hold_y_show})")

# cv2.circle(wall_img, tuple(first_hold), 4, (0, 0, 255), -1)
text = f"{first_hold_name} : ({first_hold_x}, {first_hold_y_show})"
cv2.putText(wall_img, text, (first_hold[0] + 20, first_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

# Position of Second hold

second_hold_x = randint(first_hold_x - 50, first_hold_x + 50)

second_hold_y = randint(first_hold_y - 50, first_hold_y - 30)

second_hold = [second_hold_x, second_hold_y]

second_hold_y_show = wall_height - second_hold_y

# Placing second hold image on the wall image

# Finding a random hold from the holds_list for the second hold

hold_ind = randint(0, len(holds_list) - 1)

second_hold_list = holds_list[hold_ind]
second_hold_image = holds_list[hold_ind][0]
second_hold_name = holds_list[hold_ind][2]

second_hold_width = second_hold_list[1][0]
second_hold_height = second_hold_list[1][1]

value_for_x = second_hold_width // 2
value_for_y = second_hold_height // 2
     
# top left corner x & y coordinates for the image of second hold

second_hold_img_tl_x = second_hold_x - value_for_x
second_hold_img_tl_y = second_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of second hold

second_hold_img_br_x = second_hold_x + value_for_x
second_hold_img_br_y = second_hold_y + value_for_y

# print(f"second Hold Image Coords : {second_hold_img_tl_x, second_hold_img_tl_y}, {second_hold_img_br_x, second_hold_img_br_y}")

wall_img[second_hold_img_tl_y : second_hold_img_br_y, second_hold_img_tl_x : second_hold_img_br_x] = second_hold_image

print(f"Second Hold Name : {second_hold_name} & Second Hold Coordinates : ({second_hold_x}, {second_hold_y_show})")

# cv2.circle(wall_img, tuple(second_hold), 4, (0, 0, 255), -1)
text = f"{second_hold_name} : ({second_hold_x}, {second_hold_y_show})"
cv2.putText(wall_img, text, (second_hold[0] + 20, second_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

# Position of Third hold

third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)

third_hold_y = randint(second_hold_y - 50, second_hold_y - 30)

third_hold = [third_hold_x, third_hold_y]

third_hold_y_show = wall_height - third_hold_y

# Placing third hold image on the wall image

# Finding a random hold from the holds_list for the third hold

hold_ind = randint(0, len(holds_list) - 1)

third_hold_list = holds_list[hold_ind]
third_hold_image = holds_list[hold_ind][0]
third_hold_name = holds_list[hold_ind][2]

third_hold_width = third_hold_list[1][0]
third_hold_height = third_hold_list[1][1]

value_for_x = third_hold_width // 2
value_for_y = third_hold_height // 2
     
# top left corner x & y coordinates for the image of third hold

third_hold_img_tl_x = third_hold_x - value_for_x
third_hold_img_tl_y = third_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of third hold

third_hold_img_br_x = third_hold_x + value_for_x
third_hold_img_br_y = third_hold_y + value_for_y

# print(f"third Hold Image Coords : {third_hold_img_tl_x, third_hold_img_tl_y}, {third_hold_img_br_x, third_hold_img_br_y}")

wall_img[third_hold_img_tl_y : third_hold_img_br_y, third_hold_img_tl_x : third_hold_img_br_x] = third_hold_image

print(f"Third Hold Name : {third_hold_name} & Third Hold Coordinates : ({third_hold_x}, {third_hold_y_show})")

# cv2.circle(wall_img, tuple(third_hold), 4, (0, 0, 255), -1)
text = f"{third_hold_name} : ({third_hold_x}, {third_hold_y_show})"
cv2.putText(wall_img, text, (third_hold[0] + 20, third_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))
distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))

print(f"The distance between first & third hold is {distance_between_first_and_third}")
print(f"The distance between second & third hold is {distance_between_second_and_third}")

# Position of Fourth hold

fourth_hold_x = randint(third_hold_x - 50, third_hold_x + 50)

fourth_hold_y = randint(third_hold_y - 50, third_hold_y - 30)

fourth_hold = [fourth_hold_x, fourth_hold_y]

fourth_hold_y_show = wall_height - fourth_hold_y

# Placing fourth hold image on the wall image

# Finding a random hold from the holds_list for the fourth hold

hold_ind = randint(0, len(holds_list) - 1)

fourth_hold_list = holds_list[hold_ind]
fourth_hold_image = holds_list[hold_ind][0]
fourth_hold_name = holds_list[hold_ind][2]

fourth_hold_width = fourth_hold_list[1][0]
fourth_hold_height = fourth_hold_list[1][1]

value_for_x = fourth_hold_width // 2
value_for_y = fourth_hold_height // 2
     
# top left corner x & y coordinates for the image of fourth hold

fourth_hold_img_tl_x = fourth_hold_x - value_for_x
fourth_hold_img_tl_y = fourth_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of fourth hold

fourth_hold_img_br_x = fourth_hold_x + value_for_x
fourth_hold_img_br_y = fourth_hold_y + value_for_y

# print(f"fourth Hold Image Coords : {fourth_hold_img_tl_x, fourth_hold_img_tl_y}, {fourth_hold_img_br_x, fourth_hold_img_br_y}")

wall_img[fourth_hold_img_tl_y : fourth_hold_img_br_y, fourth_hold_img_tl_x : fourth_hold_img_br_x] = fourth_hold_image

print(f"Fourth Hold Name : {fourth_hold_name} & Fourth Hold Coordinates : ({fourth_hold_x}, {fourth_hold_y_show})")

# cv2.circle(wall_img, tuple(fourth_hold), 4, (0, 0, 255), -1)
text = f"{fourth_hold_name} : ({fourth_hold_x}, {fourth_hold_y_show})"
cv2.putText(wall_img, text, (fourth_hold[0] + 20, fourth_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_third_and_fourth = euclidean(np.array(third_hold), np.array(fourth_hold))
distance_between_second_and_fourth = euclidean(np.array(second_hold), np.array(fourth_hold))
distance_between_first_and_fourth = euclidean(np.array(first_hold), np.array(fourth_hold))

print(f"The distance between third & fourth hold is {distance_between_third_and_fourth}")
print(f"The distance between second & fourth hold is {distance_between_second_and_fourth}")
print(f"The distance between first & fourth hold is {distance_between_first_and_fourth}")

# Position of fifth hold

fifth_hold_x = randint(fourth_hold_x - 50, fourth_hold_x + 50)

fifth_hold_y = randint(fourth_hold_y - 50, fourth_hold_y - 30)

fifth_hold = [fifth_hold_x, fifth_hold_y]

fifth_hold_y_show = wall_height - fifth_hold_y

# Placing fifth hold image on the wall image

# Finding a random hold from the holds_list for the fifth hold

hold_ind = randint(0, len(holds_list) - 1)

fifth_hold_list = holds_list[hold_ind]
fifth_hold_image = holds_list[hold_ind][0]
fifth_hold_name = holds_list[hold_ind][2]

fifth_hold_width = fifth_hold_list[1][0]
fifth_hold_height = fifth_hold_list[1][1]

value_for_x = fifth_hold_width // 2
value_for_y = fifth_hold_height // 2
     
# top left corner x & y coordinates for the image of fifth hold

fifth_hold_img_tl_x = fifth_hold_x - value_for_x
fifth_hold_img_tl_y = fifth_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of fifth hold

fifth_hold_img_br_x = fifth_hold_x + value_for_x
fifth_hold_img_br_y = fifth_hold_y + value_for_y

# print(f"fifth Hold Image Coords : {fifth_hold_img_tl_x, fifth_hold_img_tl_y}, {fifth_hold_img_br_x, fifth_hold_img_br_y}")

wall_img[fifth_hold_img_tl_y : fifth_hold_img_br_y, fifth_hold_img_tl_x : fifth_hold_img_br_x] = fifth_hold_image

print(f"Fifth Hold Name : {fifth_hold_name} & Fifth Hold Coordinates : ({fifth_hold_x}, {fifth_hold_y_show})")

# cv2.circle(wall_img, tuple(fifth_hold), 4, (0, 0, 255), -1)
text = f"{fifth_hold_name} : ({fifth_hold_x}, {fifth_hold_y_show})"
cv2.putText(wall_img, text, (fifth_hold[0] + 20, fifth_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_fourth_and_fifth = euclidean(np.array(fourth_hold), np.array(fifth_hold))
distance_between_third_and_fifth = euclidean(np.array(third_hold), np.array(fifth_hold))
distance_between_second_and_fifth = euclidean(np.array(second_hold), np.array(fifth_hold))
distance_between_first_and_fifth = euclidean(np.array(first_hold), np.array(fifth_hold))

print(f"The distance between fourth & fifth hold is {distance_between_fourth_and_fifth}")
print(f"The distance between third & fifth hold is {distance_between_third_and_fifth}")
print(f"The distance between second & fifth hold is {distance_between_second_and_fifth}")
print(f"The distance between first & fifth hold is {distance_between_first_and_fifth}")

# Position of sixth hold

sixth_hold_x = randint(fifth_hold_x - 50, fifth_hold_x + 50)

sixth_hold_y = randint(fifth_hold_y - 50, fifth_hold_y - 30)

sixth_hold = [sixth_hold_x, sixth_hold_y]

sixth_hold_y_show = wall_height - sixth_hold_y

# Placing sixth hold image on the wall image

# Finding a random hold from the holds_list for the sixth hold

hold_ind = randint(0, len(holds_list) - 1)

sixth_hold_list = holds_list[hold_ind]
sixth_hold_image = holds_list[hold_ind][0]
sixth_hold_name = holds_list[hold_ind][2]

sixth_hold_width = sixth_hold_list[1][0]
sixth_hold_height = sixth_hold_list[1][1]

value_for_x = sixth_hold_width // 2
value_for_y = sixth_hold_height // 2
     
# top left corner x & y coordinates for the image of sixth hold

sixth_hold_img_tl_x = sixth_hold_x - value_for_x
sixth_hold_img_tl_y = sixth_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of sixth hold

sixth_hold_img_br_x = sixth_hold_x + value_for_x
sixth_hold_img_br_y = sixth_hold_y + value_for_y

# print(f"sixth Hold Image Coords : {sixth_hold_img_tl_x, sixth_hold_img_tl_y}, {sixth_hold_img_br_x, sixth_hold_img_br_y}")

wall_img[sixth_hold_img_tl_y : sixth_hold_img_br_y, sixth_hold_img_tl_x : sixth_hold_img_br_x] = sixth_hold_image

print(f"Sixth Hold Name : {sixth_hold_name} & Sixth Hold Coordinates : ({sixth_hold_x}, {sixth_hold_y_show})")

# cv2.circle(wall_img, tuple(sixth_hold), 4, (0, 0, 255), -1)
text = f"{sixth_hold_name} : ({sixth_hold_x}, {sixth_hold_y_show})"
cv2.putText(wall_img, text, (sixth_hold[0] + 20, sixth_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_fifth_and_sixth = euclidean(np.array(fifth_hold), np.array(sixth_hold))
distance_between_fourth_and_sixth = euclidean(np.array(fourth_hold), np.array(sixth_hold))
distance_between_third_and_sixth = euclidean(np.array(third_hold), np.array(sixth_hold))
distance_between_second_and_sixth = euclidean(np.array(second_hold), np.array(sixth_hold))
distance_between_first_and_sixth = euclidean(np.array(first_hold), np.array(sixth_hold))

print(f"The distance between fifth & sixth hold is {distance_between_fifth_and_sixth}")
print(f"The distance between fourth & sixth hold is {distance_between_fourth_and_sixth}")
print(f"The distance between third & sixth hold is {distance_between_third_and_sixth}")
print(f"The distance between second & sixth hold is {distance_between_second_and_sixth}")
print(f"The distance between first & sixth hold is {distance_between_first_and_sixth}")

# Position of seventh hold

seventh_hold_x = randint(sixth_hold_x - 50, sixth_hold_x + 50)

seventh_hold_y = randint(sixth_hold_y - 50, sixth_hold_y - 30)

seventh_hold = [seventh_hold_x, seventh_hold_y]

seventh_hold_y_show = wall_height - seventh_hold_y

# Placing seventh hold image on the wall image

# Finding a random hold from the holds_list for the seventh hold

hold_ind = randint(0, len(holds_list) - 1)

seventh_hold_list = holds_list[hold_ind]
seventh_hold_image = holds_list[hold_ind][0]
seventh_hold_name = holds_list[hold_ind][2]

seventh_hold_width = seventh_hold_list[1][0]
seventh_hold_height = seventh_hold_list[1][1]

value_for_x = seventh_hold_width // 2
value_for_y = seventh_hold_height // 2
     
# top left corner x & y coordinates for the image of seventh hold

seventh_hold_img_tl_x = seventh_hold_x - value_for_x
seventh_hold_img_tl_y = seventh_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of seventh hold

seventh_hold_img_br_x = seventh_hold_x + value_for_x
seventh_hold_img_br_y = seventh_hold_y + value_for_y

# print(f"seventh Hold Image Coords : {seventh_hold_img_tl_x, seventh_hold_img_tl_y}, {seventh_hold_img_br_x, seventh_hold_img_br_y}")

wall_img[seventh_hold_img_tl_y : seventh_hold_img_br_y, seventh_hold_img_tl_x : seventh_hold_img_br_x] = seventh_hold_image

print(f"Seventh Hold Name : {seventh_hold_name} & Seventh Hold Coordinates : ({seventh_hold_x}, {seventh_hold_y_show})")

# cv2.circle(wall_img, tuple(seventh_hold), 4, (0, 0, 255), -1)
text = f"{seventh_hold_name} : ({seventh_hold_x}, {seventh_hold_y_show})"
cv2.putText(wall_img, text, (seventh_hold[0] + 20, seventh_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_sixth_and_seventh = euclidean(np.array(sixth_hold), np.array(seventh_hold))
distance_between_fifth_and_seventh = euclidean(np.array(fifth_hold), np.array(seventh_hold))
distance_between_fourth_and_seventh = euclidean(np.array(fourth_hold), np.array(seventh_hold))
distance_between_third_and_seventh = euclidean(np.array(third_hold), np.array(seventh_hold))
distance_between_second_and_seventh = euclidean(np.array(second_hold), np.array(seventh_hold))
distance_between_first_and_seventh = euclidean(np.array(first_hold), np.array(seventh_hold))

print(f"The distance between sixth & seventh hold is {distance_between_sixth_and_seventh}")
print(f"The distance between fifth & seventh hold is {distance_between_fifth_and_seventh}")
print(f"The distance between fourth & seventh hold is {distance_between_fourth_and_seventh}")
print(f"The distance between third & seventh hold is {distance_between_third_and_seventh}")
print(f"The distance between second & seventh hold is {distance_between_second_and_seventh}")
print(f"The distance between first & seventh hold is {distance_between_first_and_seventh}")

# Position of eighth hold

eighth_hold_x = randint(seventh_hold_x - 50, seventh_hold_x + 50)

eighth_hold_y = randint(seventh_hold_y - 50, seventh_hold_y - 30)

eighth_hold = [eighth_hold_x, eighth_hold_y]

eighth_hold_y_show = wall_height - eighth_hold_y

# Placing eighth hold image on the wall image

# Finding a random hold from the holds_list for the eighth hold

hold_ind = randint(0, len(holds_list) - 1)

eighth_hold_list = holds_list[hold_ind]
eighth_hold_image = holds_list[hold_ind][0]
eighth_hold_name = holds_list[hold_ind][2]

eighth_hold_width = eighth_hold_list[1][0]
eighth_hold_height = eighth_hold_list[1][1]

value_for_x = eighth_hold_width // 2
value_for_y = eighth_hold_height // 2
     
# top left corner x & y coordinates for the image of eighth hold

eighth_hold_img_tl_x = eighth_hold_x - value_for_x
eighth_hold_img_tl_y = eighth_hold_y - value_for_y

# bottom right corner x & y coordinates for the image of eighth hold

eighth_hold_img_br_x = eighth_hold_x + value_for_x
eighth_hold_img_br_y = eighth_hold_y + value_for_y

# print(f"eighth Hold Image Coords : {eighth_hold_img_tl_x, eighth_hold_img_tl_y}, {eighth_hold_img_br_x, eighth_hold_img_br_y}")

wall_img[eighth_hold_img_tl_y : eighth_hold_img_br_y, eighth_hold_img_tl_x : eighth_hold_img_br_x] = eighth_hold_image

print(f"Eighth Hold Name : {eighth_hold_name} & Eighth Hold Coordinates : ({eighth_hold_x}, {eighth_hold_y_show})")

# cv2.circle(wall_img, tuple(eighth_hold), 4, (0, 0, 255), -1)
text = f"{eighth_hold_name} : ({eighth_hold_x}, {eighth_hold_y_show})"
cv2.putText(wall_img, text, (eighth_hold[0] + 20, eighth_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)

distance_between_seventh_and_eighth = euclidean(np.array(seventh_hold), np.array(eighth_hold))
distance_between_sixth_and_eighth = euclidean(np.array(sixth_hold), np.array(eighth_hold))
distance_between_fifth_and_eighth = euclidean(np.array(fifth_hold), np.array(eighth_hold))
distance_between_fourth_and_eighth = euclidean(np.array(fourth_hold), np.array(eighth_hold))
distance_between_third_and_eighth = euclidean(np.array(third_hold), np.array(eighth_hold))
distance_between_second_and_eighth = euclidean(np.array(second_hold), np.array(eighth_hold))
distance_between_first_and_eighth = euclidean(np.array(first_hold), np.array(eighth_hold))

print(f"The distance between seventh & eighth hold is {distance_between_seventh_and_eighth}")
print(f"The distance between sixth & eighth hold is {distance_between_sixth_and_eighth}")
print(f"The distance between fifth & eighth hold is {distance_between_fifth_and_eighth}")
print(f"The distance between fourth & eighth hold is {distance_between_fourth_and_eighth}")
print(f"The distance between third & eighth hold is {distance_between_third_and_eighth}")
print(f"The distance between second & eighth hold is {distance_between_second_and_eighth}")
print(f"The distance between first & eighth hold is {distance_between_first_and_eighth}")

# resizing the wall image

wall_img_resized = cv2.resize(wall_img, (0, 0), fx=2, fy=1.5)

cv2.imshow("RouteKraft", wall_img_resized)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()



