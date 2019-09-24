
# A fuction that takes the radius of a circle as an integer, and calculates the total area of a circle with that radius
def calculateAreaOfCircle(radius):
    print("The total area of your circle is" ,3.14*radius*2)

# A function that takes two integers, the first for "miles" and the second for "gallons", then determines how many miles per gallons there are
def calculateMpg(miles, gallons):
    print("Your car's miles per gallons is" ,miles/gallons)

# A function that takes a temperature in fahrenheit as an integer, then converts it to celsius.
def convertFahrenheitToCelsius(fahrenheit):
    print("The temperature in celsius is", (fahrenheit-32)*5/9)

# A fuction that takes the X and Y cordinates of a point as two integers, then again for a second point. Then it calculates the distance between the two points.
def calculateDistanceBetweenPoints(x1, y1, x2, y2):
    from math import sqrt
    print("The distance between the two points is", sqrt((x1-x2)**2+(y1-y2)**2))