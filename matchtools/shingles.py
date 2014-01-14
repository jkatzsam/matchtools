# -*- coding: utf-8 -*-

"""shingles.py: Return the shingles of an object (e.g., string or list)."""

__author__ = "Russell J. Funk"
__date__ = "February 7, 2013"
__copyright__ = "Copyright (C) 2013"
__status__ = "Prototype"

# built in modules

# third party modules

# custom modules

def shingles(s, k_min, k_max):
	"""Return the shingles between and including size k min and k max for some 
	object s.
  
	Args:
		s: a string or a list.
		k_min: 
		k_max: 
		
	Returns:
	"""
	n = len(s)
	sh = []
	for k in xrange(k_min, k_max + 1):
		for i in xrange(n):
			if i + k <= n:
				sh.append(s[i:i+k])
	return sh