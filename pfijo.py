from math import *

def f_func_4(x):
	return (x ** 2) / 4 - sin(x)

def g_func_4(x):
	return 2 * sqrt(sin(x))


def f_func_5(x):
	return exp(x / 4) - x

def g_func_5(x):
	return exp(x / 4)


def f_func_7(x):
	return cos(x) - x

def g_func_7(x):
	return cos(x)


def f_func_18(x):
	return sin(x) - 0.5 * sqrt(x)

def g_func_18(x):
	return x - f_func_18(x)


# def iteraciones(a, b, x0, err, k):
# 	numerador = log(err) - log(max(x0 - a, b - x0))
# 	denominador = log(k)
# 	# return ceil(numerador / denominador) 
# 	return inf

def punto_fijo(a, b, x0, err, k, f_func, g_func):
	i = 0
	# n = iteraciones(a, b, x0, err, k)
	
	x1 = g_func(x0)
	print(f"P{i} = {x0} \t| f(P{i}) = {f_func(x0)}\n")
	while abs(x1 - x0) / abs(x1) >= err:
		x0 = x1
		i += 1
		x1 = g_func(x0)
		print(f"P{i} = g(P{i - 1}) = {x0} \t| f(P{i}) = {f_func(x0)}\n")
	x0 = x1
	i += 1
	print(f"P{i} = g(P{i - 1}) = {x0} \t| f(P{i}) = {f_func(x0)}\n")

# punto_fijo(1.5, 2, 1.75, 0.000001, 0.44, f_func_4, g_func_4) # 4 | Gráfico => https://www.geogebra.org/calculator/cemvnueb (espiral)
# punto_fijo(1, 1.5, 1.25, 0.001, 0.36, f_func_5, g_func_5) # 5 | Gráfico => https://www.geogebra.org/calculator/qztgyww9 (escalera)
# punto_fijo(0, 1, 0.5, 10 ** -10, 0.84, f_func_7, g_func_7) # 7
punto_fijo(0.1, 0.5, 0.3, 10 ** -2, 0.796, f_func_18, g_func_18) # 18