# Define a function calc_pyramid_volume with parameters base_length, base_width, and pyramid_height, 
# that returns as a number the volume of a pyramid with a rectangular base.

def calc_pyramid_volume(base_length, base_width, pyramid_height):
    volume = (base_length * base_width * pyramid_height) / 3
    return volume
    
length = float(input())
width = float(input())
height = float(input())
print(f'Volume for {length} {width} {height} is: {calc_pyramid_volume(length, width, height):.2f}')
