#!/usr/bin/python

import bigInt
import algs

def main():
	print "Exponentiation modulo (a^b mod m)"
	print ""
	print "Enter base (a):",
	A = bigInt.bigInt(raw_input())
	print "Enter power (b):",
	B = bigInt.bigInt(raw_input())
	print "Enter modulus (m):",
	M = bigInt.bigInt(raw_input())
	
	if (A < 0) or (B < 0) or (M <= 0):
		print "A and B must be positive!"
		print "Modulus must be > 0"
		return
	
	print A, "^", B, "mod", M, "=", algs.PowMod(A, B, M)
	
if __name__ == "__main__":
	main()
