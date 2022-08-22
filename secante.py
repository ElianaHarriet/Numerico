from math import *

def f_func_16(x):
	return (x ** 2) / 4 - sin(x)

def f(x):
	return 4 * (x ** 4) - (x ** 2) + x - 3


def g_func(x0, x1, f_func):
	num = f_func(x1) * (x1 - x0)
	den = f_func(x1) - f_func(x0)
	return x1 - num / den

def secante(x0, x1, err, f_func):
	print(f"P0 = {x0} \t| f(P0) = {f_func(x0)}\nP1 = {x1} \t| f(P1) = {f_func(x1)}\n")
	i = 2
	while abs(x1 - x0) / abs(x1) >= err:
		x2 = g_func(x0, x1, f_func)
		x0 = x1
		x1 = x2
		print(f"P{i} = {x2} \t| f(P{i}) = {f_func(x2)}\n")
		i += 1
	# revisar si es necesario imprimir un valor al salir del while

# secante(1.25, 1.625, 10 ** -3, f_func_16)
secante(0.5, 0.75, 0.03, f)
