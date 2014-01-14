VERSION = (0, 1, 0)
__version__ = '.'.join(map(str, VERSION))
__author__ = "Russell J. Funk and Julian Katz-Samuels"
__author_email__ = "funk@umich.edu"
__license__ = "3-clause BSD"
__all__ = ['simhash', 'hamming', 'shingles']    

from simhash import *
from hamming import *
from shingles import *