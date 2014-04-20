#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Legendre symbol ( L(a, p) )"
	print ""
	print "Input: a, p"
	print "Output: L(a, p)"
	print "Enter a:",
	a = bigInt.bigInt(raw_input())
	print "Enter p:",
	p = bigInt.bigInt(raw_input())
	
	print "\nL(", a, ",", p, ") =", algs.LegSym(a, p)
	
if __name__ == "__main__":
	main()
