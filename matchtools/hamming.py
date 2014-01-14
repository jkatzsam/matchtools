# -*- coding: utf-8 -*-

"""hamming.py: Return the Hamming distance between two integers (bitwise)."""

__author__ = "Russell J. Funk"
__date__ = "February 7, 2013"
__copyright__ = "Copyright (C) 2013"
__reference__ = ["http://wiki.python.org/moin/BitManipulation",
                 "http://en.wikipedia.org/wiki/Hamming_distance"]
__status__ = "Prototype"


def hamming(a, b):
	"""Calculate the Hamming distance between two integers (bitwise).
  
  	Args:
      	a: a list of 1s and 0s
      	b: a list of 1s and 0s

  	Returns:
      	The hamming distance between two integers.
      
  	Raises:
      	Value Error: Inputs must have the same bit length.
    """ 
  	if len(a) != len(b):
  		raise ValueError("Inputs must have same bit length.")
  	else:
  		distance = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                distance += 1
        return distance
  		
        
def hamming_ratio(a, b, bits = 384):
	"""Calculates the hamming ratio between two integers
        represented as a list of bits.
    
    Args:
        a and b must be lists of 1s and 0s; the calculation
        is relative to the number of bits. 
        
    Returns:
    	The hamming ratio between two integers.
    """
	return float((bits - hamming(a,b)))/bits
	
