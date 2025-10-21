'''Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.

Examples
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True'''
def circle_or_square(rad, area):
	return rad**2*3.14>area/area*4 
print(circle_or_square(5, 100))
print(circle_or_square(16, 625))    #tushunolmadim shartini