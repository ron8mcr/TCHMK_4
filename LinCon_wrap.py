#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Linear congruences (ax = b mod m)"
	print ""
	print "Enter a:",
	A = bigInt.bigInt(raw_input())
	print "Enter b:",
	B = bigInt.bigInt(raw_input())
	print "Enter m:",
	M = bigInt.bigInt(raw_input())
	
	if (A < 0) or (B < 0) or (M <= 0):
		print "A and B must be positive!"
		print "Modulus must be > 0"
		return
	
	A = A % M
	B = B % M
	
	print A, "* x =", B, "mod", M
	isSolved, x = algs.LinCon(A, B, M)
	if isSolved:
		if x == -1:
			print "x - any"
		else:	# решений может быть несколько
			x.sort()
			print "x =",
			for i in range(len(x)):
				print x[i], 
	else:
		print "No solution"
	
if __name__ == "__main__":
	main()
