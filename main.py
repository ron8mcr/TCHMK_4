#!/usr/bin/python

import GCD_wrap
import GCDBin_wrap
import GCDEx_wrap

print "1 - Euclid's algorithm for computing the greatest common divisor (GCD)"
print "2 - Binary Euclid's algorithm for computing the greatest common divisor (GCD)"
print "3 - Extended Euclid's algorithm for computing the greatest common divisor (GCD)"
print "\nSelect:",

choose = input()

if choose == 1:
	GCD_wrap.main()

elif choose == 2:
	GCDBin_wrap.main()
	
elif choose == 3:
	GCDEx_wrap.main()
