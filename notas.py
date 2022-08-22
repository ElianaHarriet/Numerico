from math import *

# m = []
for i in range(1, 5):
	a = []
	for j in range(1, 5):
		a.append(round(1 / (i + j - 1), 3))
	print(a)