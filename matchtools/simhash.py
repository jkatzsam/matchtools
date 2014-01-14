# -*- coding: utf-8 -*-

"""simhash.py: This is a more advanced version of basic_simhash.py."""

__author__ = "Russell J. Funk"
__date__ = "February 7, 2013"
__copyright__ = "Copyright (C) 2013"
__status__ = "Prototype"

# built in modules
import hashlib

# third party modules

# custom modules
import shingles
import hamming


def simhash(features):
    """Obtain a hash value for each feature.
  
    Args:
        features: an iterable. 
  
    Returns:
        A simhash
    """
    HASH_BITS = 384
    v = [0]*HASH_BITS
    for feature in features:
        feature_hash = list(bin(int(hashlib.sha384(feature).hexdigest(), 16)))
        feature_hash = feature_hash[2:]
        for i in xrange(HASH_BITS):	 
            if i >= len(feature_hash) or feature_hash[i] == '0':
                v[i] -= 1
            else:
                v[i] += 1            
    output = []
    for j in v:
        if j > 0:
            output.append(1)
        else:
            output.append(0)
    return output

	
def sim_score(str_1, str_2, chunksize = 2):
    """Compute the hamming distance ratio between two strings
  
    Args:
        str_1: a string
        str_2: a string
        chunksize: The length of the string chunks that are treated as features
  
    Returns:
        A number between 0 and 1
    """
    tokens_1 = [str_1[i: i + chunksize] for i in range(0,len(str_1), chunksize)]
    tokens_2 = [str_2[i: i + chunksize] for i in range(0,len(str_2), chunksize)]
    sim_1 = simhash(tokens_1)
    sim_2 = simhash(tokens_2)
    return hamming.hamming_ratio(sim_1, sim_2)

