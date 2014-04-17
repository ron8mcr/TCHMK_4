#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt

def GCD (a, b):
	if (a < b):
		return GCD (b, a)
	if b == 0:
		return a
	if a == 0:
		return b
	r = 1
	while r != 0:
		r = a % b
		a = b
		b = r
	if a < 0:
		a = -a
	return a


def GCDBin(a, b):
	if (a < b):
		return GCDBin (b, a)
	
	if a < 0:
		a = -a
	if b < 0:
		b = -b
		
	if b == 0:
		return a
	if a == 0:
		return b
	
	g = bigInt.bigInt(1)
	while (a % 2 == 0) and (b % 2 == 0):
		a /= 2
		b /= 2
		g *= 2
	
	while a != 0:
		while a % 2 == 0:
			a /= 2
		while b % 2 == 0:
			b /= 2
		if a >= b:
			a = a - b
		else:
			b = b - a
	return g * b		

	
def GCDEx(a, b):		
	if b == 0:
		return a, 1, 0
	if a == 0:
		return b, 1, 0
	
	x1 = bigInt.bigInt(0)
	x2 = bigInt.bigInt(1)
	y1 = bigInt.bigInt(1)
	y2 = bigInt.bigInt(0)
	
	while b != 0:
		q = a / b
		r = a % b
		a = b
		b = r
		
		xx = x2 - x1 * q
		yy = y2 - y1 * q
		x2 = x1
		x1 = xx
		y2 = y1
		y1 = yy
	x = x2
	y = y2

	return a, x, y

def PowMod(A, B, M):
	return bigInt.pow(A, B, M)
	
def LinCon (a, b, m):
	"Решение линейного сравнение ax = b mod m"
	d = GCD(a, m)	
	if b % d != 0:
		return False, 0
	
	if (a == 0 or b % m == 0) and (b == 0 or a % m == 0):
		return True, -1
	
	# находим одно из решений, используя расширенный алгоритм Евклида
	a1 = a / d
	b1 = b / d
	m1 = m / d
	d1, x, y = GCDEx(a1, m1)	
	res0 = ( b1 * x ) % m
	while res0 < 0:
		res0 += m

	# теперь находим оставшиеся d-1 решения
	resAll = []
	resAll.append(res0)
	d = d - 1
	while d > 0:
		resAll.append( (resAll[-1] + m1) % m )
		if resAll[-1] < 0:
			resAll[-1] += m
		d -= 1
	
	return True, resAll
	
def ChinRemTheorem(R, A):
	"Решение системы уравнений по китайской теореме об остатках"
	M = bigInt.bigInt(1)
	for Ai in A:
		M *= Ai
	
	x = bigInt.bigInt(0)
	for i in range(len(A)):
		Mi = M / A[i]
		isOK, invArr = LinCon (Mi, bigInt.bigInt(1), A[i]) # нахождение обратного для Mi
		MiInv = invArr[0] # в общем случае, у элемента может быть (?) несколько обратных, поэтому берём первый
		x = (x + R[i] * Mi * MiInv) % M
		
	return x
