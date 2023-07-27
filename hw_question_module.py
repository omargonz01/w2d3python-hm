
import math 


def square_feet_of_house():
    length = float(input("enter the length in feet")) #int didnt work #str didnt work, process of illimination = float
    width = float(input("enter the width in feet"))
    room_area = length * width
    print(f'this is the total square footage of the house {total_sq_ft}')
    return room_area


def get_circumference():
    radius = input("what is the radius")
    circumference = 2 * math.pi * radius
    print(f'The total circumference for circle with {radius} is {circumference}')
    return circumference 

