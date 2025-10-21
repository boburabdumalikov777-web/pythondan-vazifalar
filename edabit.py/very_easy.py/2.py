'''Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720'''
 
def sum_polygon(n):
	x=(n-2)*180
	return x
print(sum_polygon(3)) #➞ 180

print(sum_polygon(4)) #➞ 360

print(sum_polygon(6)) #➞ 720