#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Quadratic congruences modulo a prime ( ax^2 + bx + c = 0 mod p )"
	print ""
	print "Input: a, b, c, p (odd prime)"
	print "Output: x:\n"
	
	print "Enter a:",
	a = bigInt.bigInt(raw_input())
	print "Enter b:",
	b = bigInt.bigInt(raw_input())
	print "Enter c:",
	c = bigInt.bigInt(raw_input())
	print "Enter p:",
	p = bigInt.bigInt(raw_input())
	
	if p < 3:
		print "p must be odd prime!"
		return
		
	if not algs.isPrime(p):
		print "p must be prime!"
		return
	
	a = a % p
	if a < 0:
		a += p
	b = b % p
	if b < 0:
		b += p
	c = c % p
	if c < 0:
		c += p

	if a == 0:
		print "This is linear congruence"
		c = p - c
		print b, "* x =", c, "mod", p
		isSolved, x = algs.LinCon(b, c, p)
		if isSolved:
			if x == -1:
				print "x - any"
			else:	# решений может быть несколько
				x.sort()
				print "x =", x
		else:
			print "No solution"
		return
	
	# сокращаем на коэффициент a:
	# Вычисляем invA = a^(-1)mod p - обратный элемент в кольце Zp
	isOK, invArr = algs.LinCon (a, bigInt.bigInt(1), p)
	invA = invArr[0]
	b = (b * invA) % p
	c = (c * invA) % p
	
	if (b % 2 == 0):
		# делаем замену
		#	y = x + b/2
		#	a = (b1/2)^2 - c
		# и получаем уравнение y^2 = a
		# решаем его
		if ((b/2 * b/2 - c) % p == 0):
			print "x =", (p + 1)/2
			return
		isSolved, y = algs.SqrtPrime ( (b/2 * b/2 - c) % p, p)
		if not isSolved:
			print "No solution"
			return
		res = [0]*2
		res[0] = (y[0] - b/2) % p
		res[1] = (y[1] - b/2) % p
	else:
		# делаем замену
		#	y = x + (b + p)/2
		#	a = ((b + p) / 2)^2 - c 
		isSolved, y = algs.SqrtPrime ( ((b + p)/2 * (b + p)/2 - c) % p , p)
		if not isSolved:
			print "No solution"
			return
		res = [0]*2
		res[0] = (y[0] - (b + p)/2) % p
		res[1] = (y[1] - (b + p)/2) % p
			
	if res[0] < 0:
		res[0] += p
	if res[1] < 0:
		res[1] += p
			
	print "\nx =", res
	
if __name__ == "__main__":
	main()
