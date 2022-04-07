from math import *

def f_func_7(x):
	return cos(x) - x

def fprim_func_7(x):
	return -sin(x) - 1


def f_func_8(x):
	return x ** 2 - 1

def fprim_func_8(x):
	return 2 * x


def f_func_9(x):
	return 1 - exp(-2 * x) - x

def fprim_func_9(x):
	return 2 * exp(-2 * x) - 1


def f_func_10(x):
	return x * log(x, e) - 1

def fprim_func_10(x):
	return 1 + log(x, e)


def f_func_12(x):
	return x ** 3 - 9 * (x ** 2) + 24 * x - 20

def fprim_func_12(x):
	return 3 * (x ** 2) - 18 * x + 24


def f_func_14(x):
	return sin(x) - exp(x)

def fprim_func_14(x):
	return cos(x) - exp(x)


def f_func_15(x):
	return x ** 3 - 1.9 * (x ** 2) - 1.05 * x + 2.745

def fprim_func_15(x):
	return 3 * (x ** 2) - 3.8 * x + 1.05


def newton_raphson(x0, err, f_func, fprim_func):
	print(f"\n- - - - Newton-Raphson - - - -\nx0 = {x0}\n")
	i = 0
	
	x1 = x0 - (f_func(x0) / fprim_func(x0))
	print(f"P{i} = {x0} \t| f(P{i}) = {f_func(x0)}\n")
	while abs(x1 - x0) / abs(x1) >= err:
		x0 = x1
		i += 1
		x1 = x0 - (f_func(x0) / fprim_func(x0))
		print(f"P{i} = P{i - 1} - (f(P{i - 1}) / f'(P{i - 1})) = {x0} \t| f(P{i}) = {f_func(x0)}\n")
		
		if abs(f_func(x1)) > abs(f_func(x0)) * 4:
			print("Error: No converge")
			print("- - - - - - - - - - - - - - - -\n")
			return False
	return True



def paso_biseccion(a, b, f_func):
	x = (a + b) / 2
	if f_func(x) * f_func(a) < 0:
		b = x
	else:
		a = x
	return a, b

def main(a, b, err, f_func, fprim_func):
	print("Hace 3 pasos de biseccion")
	for _ in range(3):
		a, b = paso_biseccion(a, b, f_func)
	
	x0 = (a + b) / 2
	converge = newton_raphson(x0, err, f_func, fprim_func)
	
	if not converge:
		main(a, b, err, f_func, fprim_func)


# newton_raphson(0.5, 10 ** -10, f_func_7, fprim_func_7) # 7
# newton_raphson(2, 10 ** -10, f_func_8, fprim_func_8) # 8
# newton_raphson(0.67, 10 ** -10, f_func_9, fprim_func_9) # 9
# newton_raphson(1.5, 10 ** -10, f_func_10, fprim_func_10) # 10
# newton_raphson(1.5, 0.001, f_func_12, fprim_func_12) # 12
# newton_raphson(-9, 10 ** -6, f_func_14, fprim_func_14) # 14
newton_raphson(-1, 10 ** -6, f_func_15, fprim_func_15) # 15