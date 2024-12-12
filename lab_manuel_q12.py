# write a python program that accepts the length of 3 sides of a triangle as inputs. the program should indicate
# weather or not the triangle is right angle triangle also find out its area using heron's formula
# Function to check if the triangle is a right-angled triangle
def right_angle(sides):
    sides.sort()  # Sort the sides to identify the hypotenuse
    x, y, h = sides  # Smallest two sides (x, y) and hypotenuse (h)
    if h**2 == x**2 + y**2:  # Pythagorean theorem
        return "Right-angled"
    else:
        return "Not right-angled"

# Function to calculate the area using Heron's formula
def area(sides):
    a, b, c = sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Applying Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Input sides of the triangle
sides = [3, 4, 5]

# Check if it is a right-angled triangle
print("The triangle is:", right_angle(sides))

# Calculate and display the area
print("The area of the triangle is:", area(sides))
