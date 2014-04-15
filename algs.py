#!/usr/bin/python

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
	
