#!/usr/bin/python
# -*- coding: utf-8 -*-

import bigInt

def GCD (a, b):
	if (a < b):
		return GCD (b, a)
	if b == 0:
		return a
	if a == 0:
		return b
	r = 1
	while r != 0:
		r = a % b
		a = b
		b = r
	if a < 0:
		a = -a
	return a


def GCDBin(a, b):
	if (a < b):
		return GCDBin (b, a)
	
	if a < 0:
		a = -a
	if b < 0:
		b = -b
		
	if b == 0:
		return a
	if a == 0:
		return b
	
	g = bigInt.bigInt(1)
	while (a % 2 == 0) and (b % 2 == 0):
		a /= 2
		b /= 2
		g *= 2
	
	while a != 0:
		while a % 2 == 0:
			a /= 2
		while b % 2 == 0:
			b /= 2
		if a >= b:
			a = a - b
		else:
			b = b - a
	return g * b		

	
def GCDEx(a, b):		
	if b == 0:
		return a, 1, 0
	if a == 0:
		return b, 1, 0
	
	x1 = bigInt.bigInt(0)
	x2 = bigInt.bigInt(1)
	y1 = bigInt.bigInt(1)
	y2 = bigInt.bigInt(0)
	
	while b != 0:
		q = a / b
		r = a % b
		a = b
		b = r
		
		xx = x2 - x1 * q
		yy = y2 - y1 * q
		x2 = x1
		x1 = xx
		y2 = y1
		y1 = yy
	x = x2
	y = y2

	return a, x, y

def PowMod(A, B, M):
	return bigInt.pow(A, B, M)
	
def LinCon (a, b, m):
	"Решение линейного сравнение ax = b mod m"
	d = GCD(a, m)	
	if b % d != 0:
		return False, 0
	
	if (a == 0 and b % m == 0) or (b == 0 and a % m == 0):
		return True, -1
	
	# находим одно из решений, используя расширенный алгоритм Евклида
	a1 = a / d
	b1 = b / d
	m1 = m / d
	d1, x, y = GCDEx(a1, m1)	
	res0 = ( b1 * x ) % m
	while res0 < 0:
		res0 += m

	# теперь находим оставшиеся d-1 решения
	resAll = []
	resAll.append(res0)
	d = d - 1
	while d > 0:
		resAll.append( (resAll[-1] + m1) % m )
		if resAll[-1] < 0:
			resAll[-1] += m
		d -= 1
	
	return True, resAll
	
def ChinRemTheorem(R, A):
	"Решение системы уравнений по китайской теореме об остатках"
	M = bigInt.bigInt(1)
	for Ai in A:
		M *= Ai
	
	x = bigInt.bigInt(0)
	for i in range(len(A)):
		Mi = M / A[i]
		isOK, invArr = LinCon (Mi, bigInt.bigInt(1), A[i]) # нахождение обратного для Mi
		MiInv = invArr[0] # в общем случае, у элемента может быть (?) несколько обратных, поэтому берём первый
		x = (x + R[i] * Mi * MiInv) % M
		
	return x
	
def GarnersAlg(R, A):
	"Решение системы линейных сравнений по алгоритму Гарнера"
	# инициализируем массив inverses, inverses[j,i] = aj^(-1) mod ai
	
	inverses = []
	for i in range(len(A)):
    		inverses.append([bigInt.bigInt(0)] * len(A))
    	
    	for i in range (len(A)):
    		for j in range (i):
    			isOK, invArr = LinCon (A[j], bigInt.bigInt(1), A[i]) # нахождение обратного для A[i]
			inverses[j][i] = invArr[0]
	
	# подсчитываем коэффициенты по алгоритму Гарнера
	x = [bigInt.bigInt(0)] * len(A)
	for i in range (len(A)):
		x[i] = R[i]
    		for j in range (i):
			x[i] = inverses[j][i] * (x[i] - x[j])
			x[i] = x[i] % A[i];
			if x[i] < 0:
				x[i] += A[i]
	
	return x
	
 
# Для алгоритма Ро-полларда
# алгоритм с http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms
def new_xab(x, a, b, n, N, alpha, beta):
	c = x % 3
	if c == 0:
		x = (x*x) % N
		a = (a*2) % n 
		b = (b*2) % n
	elif c == 1:
		x = x*alpha % N
		a = (a+1) % n
	elif c == 2:
		x = x*beta % N
		b = (b+1) % n

	return x, a, b 

def RhoPollard(alpha, beta, N):
	n = N - 1
	x = bigInt.bigInt(1)
	a = bigInt.bigInt(0)
	b = bigInt.bigInt(0)
	X = x
	A = a
	B = b
	
	i = bigInt.bigInt(1)
	while (i < n):
		x, a, b = new_xab( x, a, b, n, N, alpha, beta )
		X, A, B = new_xab( X, A, B, n, N, alpha, beta )
		X, A, B = new_xab( X, A, B, n, N, alpha, beta )
		i += 1
		if( x == X and i > 2):
			if (B - b) == 0:
				return None
			Bb = B - b
			Aa = A - a
			if Bb < 0:
				Bb = b - B
			if Aa < 0:
				Aa = a - A
				
			isSolved, res = LinCon(Bb, Aa, n)
			if not isSolved:
				return None
			if res == -1:
				return None
			return res[0]
			
def LegSym (a, p):
	if a == -1:
		if ((p - 1) / 2) % 2 == 0:
			return 1
		else:
			return -1	
			
	if a == 1:
		return 1
			
	if a < 0:
		return LegSym(-1, p) * LegSym (-a, p)
	
	a %= p
	
	if a == 0:
		return 1
		
	if a % 2 == 0:
		if ((p*p - 1) / 8) % 2 == 0:
			return LegSym (a/2, p)
		else:
			return -1 * LegSym (a/2, p)
			
	if a % 4 == 3 and p % 4 == 3: # !((a - 1)/2 * (p - 1)/2 ) % 2 == 0
		return -1 *LegSym(p, a)
	else:
		return LegSym (p, a)	
		
def JacobiSym (a, p):
	if GCD (a, p) != 1:
		return 0
		
	r = bigInt.bigInt(1)
	
	if a < 0:
		a = -a
		if p % 4 == 3:
			r = -r
	
	while (a != 0):
		t = bigInt.bigInt(0)
		while a % 2 == 0:
			t += 1
			a = a / 2
		if t % 2 == 1:
			if p % 8 == 3 or p % 8 == 5:
				r = -r
	
		if a % 4 == 3 and p % 4 == 3:
			r = -r
		c = a
		a = p % c
		p = c
	return r
	
def TrialDiv (n):
	if n < 0:
		n = -n
	i = 2
	while i <= (n+1)/2:
		if n % i == 0:
			return i
		i += 1
	return 1
	
def isPrime (n):
	if TrialDiv(n) == 1:
		return True
	else:
		return False
		
def SqrtPrime (a, p):
	"Нахождение квадратного корня по модулю простого числа по алгоритму Тонелли-Шенкса"
	# проверка, есть ли вообще решение
	if JacobiSym(a, p) == -1:
		return False, 0
		
	# находим b такое что (b,p)=-1 
	b = bigInt.bigInt(2)
	while (JacobiSym(b, p) == 1):
		b += 1
		
	# Представляем p-1 в виде p-1 = 2^s*t, где t - нечетное
	t = p - 1
	s = bigInt.bigInt(0)
	while (t % 2 == 0):
		t /= 2
		s += 1
	
# по методичке Шитова	
#	# Вычисляем a2 = a^(-1)mod p - обратный элемент в кольце Zp
#	isOK, invArr = LinCon (a, bigInt.bigInt(1), p)
#	a2 = invArr[0]
#	
#	N1 = PowMod (b, t, p)
#	a1 = PowMod (a, (t + 1)/2, p)
#	N2 = bigInt.bigInt(1)
#	j = 0
#	
#	i = bigInt.bigInt(0)
#	while i < s - 1:
#		b = (a1 * N2) % p
#		c = (a2 * b * b) % p
#		
#		e = PowMod(bigInt.bigInt(2), s - 2 - i, p)
#		d = PowMod (c, e, p)
#		
#		if d == 1:
#			j = 0
#		if d == p - 1:
#			j = 1
#		e = PowMod(bigInt.bigInt(2), i, p)
#		e *= j
#		N2 = (N2 * PowMod(N1, e, p)) % p
#		print "i =",i, "b =", b, "c =", c, "d =", d, "j =", j, "N2 =", N2
#		i += 1
#	res = (a1 * N2) % p
#	return True, [res, -res]

	# Вычисляем invA a^(-1)mod p - обратный элемент в кольце Zp
	isOK, invArr = LinCon (a, bigInt.bigInt(1), p)
	invA = invArr[0]
	
	c = PowMod (b, t, p)
	r = PowMod (a, (t + 1)/2, p)
	
	i = bigInt.bigInt(1)
	while i < s:
		# вычисляем d=[(r^2*invA)^(2^(s-i-1))][mod p]
		e = PowMod(bigInt.bigInt(2), s - i - 1, p)
		d = PowMod(r*r * invA, e, p)
		print "d =", d
		if d == p - 1:
			r = (r * c) % p
		c = (c * c) % p
		i += 1
	return True, [r, -r]
