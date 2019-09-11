import os
import sys

path = sys.argv[1]

def createDictWithValues(filename):
	key = 1
	dictionary = {}
	fullpath = (path + filename)
	fullpath = os.path.normpath(fullpath)
	file = open(fullpath)
	for value in file:
		value = value.rstrip('\n')
		value = float(value)
		dictionary[key] = value
		key += 1
	return dictionary

cash1 = createDictWithValues('\\Cash1.txt')
cash2 = createDictWithValues('\\Cash2.txt')
cash3 = createDictWithValues('\\Cash3.txt')
cash4 = createDictWithValues('\\Cash4.txt')
cash5 = createDictWithValues('\\Cash5.txt')

AllCash = (cash1,cash2,cash3,cash4,cash5)
cashAllPerDay = {} 
for dictionary in AllCash:
  for key in dictionary:
    try:
      cashAllPerDay[key] += dictionary[key]
    except KeyError:
      cashAllPerDay[key] = dictionary[key]

def maxValue():
	v=list(cashAllPerDay.values())
	k=list(cashAllPerDay.keys())
	return k[v.index(max(v))]
MaxVal = maxValue()
print(MaxVal)