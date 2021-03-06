#!/usr/bin/python

import bigInt
import algs

def main():
	print "Euclid's algorithm for computing the greatest common divisor ( GCD(A, B) )"
	print ""
	print "Enter A:",
	A = bigInt.bigInt(raw_input())
	print "Enter B:",
	B = bigInt.bigInt(raw_input())
	
	print "GCD (", A, ",", B, ") =", algs.GCD(A, B)
	
if __name__ == "__main__":
	main()
