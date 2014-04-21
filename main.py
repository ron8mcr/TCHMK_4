#!/usr/bin/python

import GCD_wrap
import GCDBin_wrap
import GCDEx_wrap
import PowMod_wrap
import LinCon_wrap
import ChineseRemTheorem_wrap
import GarnersAlg_wrap
import RhoPollard_wrap
import LegendreSymbol_wrap
import JacobiSymbol_wrap
import SqrtPrime_wrap
import QuadConPrime_wrap

print "Welcome!"
print "Select the menu item:"
print ""
print "1 - Euclid's algorithm for computing the greatest common divisor ( GCD(A, B) )"
print "2 - Binary Euclid's algorithm for computing the greatest common divisor ( GCD(A, B) )"
print "3 - Extended Euclid's algorithm for computing the greatest common divisor ( GCD(A, B) )"
print "4 - Exponentiation modulo (a^b mod m)"
print "5 - Linear congruences (ax = b mod m)"
print "6 - Chinese remainder theorem"
print "7 - Garner's algorithm"
print "8 - Pollard's rho algorithm for logarithms (a^x = b mod m)"
print "9 - Legendre symbol ( L(a, p) )"
print "10 - Jacobi symbol ( J(a, p) )"
print "11 - Square root modulo a prime ( x^2 = a mod p (p - prime) )"
print "12 - Quadratic congruences modulo a prime ( ax^2 + bx + c = 0 mod p )"
print ""
print "Select:",

choose = input()
print ""

if choose == 1:
	GCD_wrap.main()

elif choose == 2:
	GCDBin_wrap.main()
	
elif choose == 3:
	GCDEx_wrap.main()
	
elif choose == 4:
	PowMod_wrap.main()
	
elif choose == 5:
	LinCon_wrap.main()
	
elif choose == 6:
	ChineseRemTheorem_wrap.main()

elif choose == 7:
	GarnersAlg_wrap.main()
	
elif choose == 8:
	RhoPollard_wrap.main()
	
elif choose == 9:
	LegendreSymbol_wrap.main()
	
elif choose == 10:
	JacobiSymbol_wrap.main()
	
elif choose == 11:
	SqrtPrime_wrap.main()
	
elif choose == 12:
	QuadConPrime_wrap.main()	
