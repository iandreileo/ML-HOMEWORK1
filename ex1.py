import math

from tests.beam_tests import run_beam_tests
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *


if __name__ == '__main__':

    run_beam_tests()
