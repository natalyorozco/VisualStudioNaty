import math
radius = int (input ("Enter the radius of the circle: "))
depth = int (input ("Enter depth: "))
area = math.pi* (radius**2)
volume = area*depth
print (round (volume, 3))