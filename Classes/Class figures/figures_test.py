import figures 


# a square with size = 2 units
square1 = figures.square(2)

# a circle with radius = 5 units
circle1 = figures.circle(5)

# a right-trianguel with base = 4 units and height = 3 units
triangle1 = figures.right_triangle(4,3)


print("The square 1 has a size = ",square1.size," and a perimeter = ",square1.perimeter)
print("The circle 1 has a radius = ",circle1.radius," and a perimeter = ",circle1.perimeter)
print("The triangle 1 has a base = ",triangle1.base," a height = ",triangle1.height," and an area = ",triangle1.area)
