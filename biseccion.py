from math import *

def func_1(x):
	return exp(x) * (sin(x) + cos(x) - 2 * x - 2)

def func_2a(x):
	return x * cos(x) - log(x, e)

def func_2b(x):
	return 2 * x - exp(-x)

def func_2c(x):
	return 1 - x - exp(-2 * x)

def func_3(x):
	return (x ** 2) / 4 - sin(x)

def pn(a, b):
	return (a + b) / 2

def iteraciones(a, b, err):
	# return ceil((log(b - a, e) - log(err, e)) / log(2, e))
	return inf

def bisection(a, b, err, func):
	x0 = inf
	x1 = pn(a, b)
	print(f"P1 = {x1} \t| f(P1) = {func(x1)}\n")

	n = iteraciones(a, b, err)
	i = 2
	while abs(x1 - x0) / abs(x1) > err and i <= n:
	# while abs(x1 - x0) > err and i <= n:
		if func(a) * func(x1) < 0:
			print(f"f(a{i - 1}) * f(P{i - 1}) < 0 | a{i} = a{i - 1}, b{i} = P{i - 1}")
			b = x1
		else:
			print(f"f(P{i - 1}) * f(b{i - 1}) < 0 | a{i} = P{i - 1}, b{i} = b{i - 1}")
			a = x1
		x0 = x1
		x1 = pn(a, b)
		print(f"P{i} = {x1} \t| f(P{i}) = {func(x1)}")
		# print(abs(x1 - x0))
		print(abs(x1 - x0) / abs(x1))
		print()
		i += 1
	return x1

# bisection(-2.5, -0.5, 0.00001, func_1) # 1
# bisection(0 + 10 ** -10, 1.6 - 10 ** -10, 0.02, func_2a) # 2a
# bisection(0 + 10 ** -10, 1.6 - 10 ** -10, 0.02, func_2b) # 2b
# bisection(0 + 10 ** -10, 1.6 - 10 ** -10, 0.02, func_2c) # 2c
bisection(0, 2, 0.02, func_3) # 3