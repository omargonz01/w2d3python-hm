
def square_feet_of_house(length, width):
    room_area = length * width
    return room_area

length = float(input("enter the length in feet")) #int didnt work #str didnt work, process of illimination = float
width = float(input("enter the width in feet"))


total_sq_ft = square_feet_of_house(length, width)

print(f'this is the total square footage of the house {total_sq_ft}')



import math 

def get_circumference():
    circumference = 2 * math.pi * radius
    return circumference 

radius = input("what is the radius")

circumference = get_circumference(radius)
print(f'The total circumference for circle with {radius} is {circumference}')
