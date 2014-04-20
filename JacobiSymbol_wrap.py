#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Jacobi symbol ( J(a, p) )"
	print ""
	print "Input: a, p"
	print "Output: J(a, p)\n"
	
	print "Enter a:",
	a = bigInt.bigInt(raw_input())
	print "Enter p:",
	p = bigInt.bigInt(raw_input())
	
	print "\nJ(", a, ",", p, ") =", algs.JacobiSym(a, p)
	
if __name__ == "__main__":
	main()
