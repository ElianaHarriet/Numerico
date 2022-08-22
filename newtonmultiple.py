from math import *

def f_func_12(x):
	return x ** 3 - 9 * (x ** 2) + 24 * x - 20

def fprim_func_12(x):
	return 3 * (x ** 2) - 18 * x + 24

def fprimprim_func_12(x):
	return 6 * x - 18


def g_func(x0, f_func, fprim_func, fprimprim_func):
	num = f_func(x0) * fprim_func(x0)
	den = fprim_func(x0) ** 2 - f_func(x0) * fprimprim_func(x0)
	return x0 - num / den

def newton_raphson_mul(x0, err, f_func, fprim_func, fprimprim_func):
	print(f"\n- - - - Newton-Raphson - - - -\nx0 = {x0}\n")
	i = 0
	
	x1 = g_func(x0, f_func, fprim_func, fprimprim_func)
	print(f"P{i} = {x0} \t| f(P{i}) = {f_func(x0)}\n")
	while abs(x1 - x0) / abs(x1) > err:
		x0 = x1
		i += 1
		x1 = g_func(x0, f_func, fprim_func, fprimprim_func)
		print(f"P{i} = {x0} \t| f(P{i}) = {f_func(x0)}\n")
		
		if abs(f_func(x1)) > abs(f_func(x0)) * 4:
			print("Error: No converge")
			print("- - - - - - - - - - - - - - - -\n")
			return False
	x0 = x1
	i += 1
	print(f"P{i} = {x0} \t| f(P{i}) = {f_func(x0)}\n")
	return True


newton_raphson_mul(1.5, 0.001, f_func_12, fprim_func_12, fprimprim_func_12) #12