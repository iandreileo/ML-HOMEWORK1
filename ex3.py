import math
from glds import GLDS
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *
import sys
import time
import resource
from tests.blds_tests import run_blds_tests

from tests.glds_tests import run_glds_tests

sys.setrecursionlimit(10 ** 7)

if __name__ == '__main__':

    run_blds_tests()


