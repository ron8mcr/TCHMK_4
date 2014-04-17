#!/usr/bin/python

import bigInt
import algs

def main():
	print "Extended Euclid's algorithm for computing the greatest common divisor ( GCD(A, B) )"
	print "Enter A:",
	A = bigInt.bigInt(raw_input())
	print "Enter B:",
	B = bigInt.bigInt(raw_input())
	
	if (A < 0) or (B < 0):
		print "A and B must be positive!"
		return
	
	if A > B:
		GCD, X, Y = algs.GCDEx(A, B)
	else:
		GCD, Y, X = algs.GCDEx(B, A)
		
	print "GCD (", A, ",", B, ") =", GCD, "=", X, "*", A, "+", Y, "*", B  
	
if __name__ == "__main__":
	main()
