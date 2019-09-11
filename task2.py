import sys
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pathForRectangleDots = sys.argv[1]
pathForDots = sys.argv[2]
arrayWithRectangleDots = []
arrayWithDots = []

fileWithRectangleDots = open('{0}.txt'.format(pathForRectangleDots))
for value in fileWithRectangleDots:
	value = value.rstrip('\n')
	value = value.split(' ')
	floatArr =[]
	for num in value:
		num = float(num)
		floatArr.append(num)
	arrayWithRectangleDots.append(floatArr)

fileWithDots = open('{0}.txt'.format(pathForDots))
for value in fileWithDots:
	value = value.rstrip('\n')
	value = value.split(' ')
	floatArr =[]
	for num in value:
		num = float(num)
		floatArr.append(num)
	arrayWithDots.append(floatArr)

point1, point2, point3, point4 = arrayWithRectangleDots
for dot in arrayWithDots:
	if point1 == dot or point2 == dot or point3 == dot or point4 == dot:
		print('0')
	elif (point1[0] <= dot[0] <= point2[0] and point1[1] <= dot[1] <= point2[1]):
		print('1')
	elif (point2[0] <= dot[0] <= point3[0] and point2[1] <= dot[1] <= point3[1]):
		print('1')
	elif (point3[0] <= dot[0] <= point4[0] and point3[1] <= dot[1] <= point4[1]):
		print('1')
	elif (point4[0] <= dot[0] <= point1[0] and point4[1] <= dot[1] <= point1[1]):
		print('1')
	elif point1[0] <= dot[0] <= point3[0] and point1[1] <= dot[1] <= point3[1]:
		print('2')
	else:
	 	print('3')