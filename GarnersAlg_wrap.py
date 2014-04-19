#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt
import algs

def main():
	print "Garner's algorithm"
	print ""
	print "X = R1 (mod A1)"
	print "X = R2 (mod A2)"
	print ". . . . . . . ."
	print "X = Rn (mod An)"
	print "X = x1 + x2 * a1 + ... + xn * a1 * ... * a(n-1) - ?"
	print "Input: n, Ri, Ai (i = 1 .. n)"
	print "Output: X, xi\n"
	
	print "Enter n:",
	n = int (input())
	
	R = [0] * n
	A = [0] * n	
	
	# Ввод Ri, Ai
	for i in range (n):
		print '\nEnter R%d:' % (i + 1),
		Ri = bigInt.bigInt(raw_input())
		print 'Enter A%d:' % (i + 1),
		Ai = bigInt.bigInt(raw_input())
		if Ai < 2:
			print "Modulus must be > 1!"
			return
		Ri %= Ai
		if Ri < 0:
			Ri += Ai
		R[i] = Ri
		A[i] = Ai
	
	# Проверка на попарную простоту Ai
	i = 0
	isSimplePairwise = True
	while i != n and isSimplePairwise:
		j = i + 1
		while j != n and isSimplePairwise:
			if algs.GCD(A[i], A[j]) != 1:
					isSimplePairwise = False
			j += 1
		i += 1
		
	if not isSimplePairwise:
		print "Modules (Ai) must be simple pairwise!"
		return
	
	print ""	
	for i in range (n):
		print "X =", R[i], "mod", A[i]
	
	print ""
	x = algs.GarnersAlg(R, A) # получаем массив коэффициентов xi
	coefAi = bigInt.bigInt(1) # a1 * a2 * ... a(i-1)
	res = bigInt.bigInt(0)    # X = x1 * a1 + ...	
	print "X =",
	for i in range (len(x)):
		res = res + x[i] * coefAi
		print x[i], "*", coefAi,
		if i != n - 1:
			print "+",
		coefAi *= A[i]
	print "=", res
		
if __name__ == "__main__":
	main()
