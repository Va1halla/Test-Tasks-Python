import sys
import numpy as n
import os

path = sys.argv[1]
os.chdir(os.path.dirname(os.path.abspath(__file__)))
arrNums = [] # list with data from file

file = open('{0}.txt'.format(path))
for value in file:
	value = value.rstrip('\n')
	arrNums.append(float(value))

readyArray = n.array(arrNums) #numpy classic array

# 90 percentile
answerPersentile = n.percentile(readyArray, 90)
answerPersentile = float(answerPersentile)
print('%.2f' % answerPersentile)

# 50 percentile (mediana)
answerMediana = n.percentile(readyArray, 50)
print('%.2f' % answerMediana)

#maximum
print('%.2f' % max(readyArray))

#minimum
print('%.2f' % min(readyArray))

#average
print('%.2f' % n.mean(readyArray))
