#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Pollard's rho algorithm for logarithms (a^x = b mod m)"
	print ""
	print "Input: a, b, m (prime)"
	print "Ouput: x\n"
	
	print "Enter a:",
	a = bigInt.bigInt(raw_input())
	print "Enter b:",
	b = bigInt.bigInt(raw_input())
	print "Enter m:",
	m = bigInt.bigInt(raw_input())
	# нужна проверка m на простоту
	# нужна проверка на порядок числа a по модулю m
	
	print ""
	print a, "^ x =", b, "mod", m
	
	x = algs.RhoPollard(a, b, m)
#	if x == None:
#		print "No solution"
#	else:
#		print "x = ", x
#	
	print "x =", x
if __name__ == "__main__":
	main()
