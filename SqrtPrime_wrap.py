#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Square root modulo a prime ( x^2 = a mod p (p - prime) )"
	print ""
	print "Input: a, p (odd prime)"
	print "Output: x: x^2 = a mod p\n"
	
	print "Enter a:",
	a = bigInt.bigInt(raw_input())
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
	if a == 0:
		print "x = 0"
		return
		
	isSolution, res = algs.SqrtPrime(a, p)
	if not isSolution:
		print "\nNo solution"
		return
	print "\nx =", res
	
if __name__ == "__main__":
	main()
