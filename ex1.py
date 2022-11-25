import math
from tests.astar_tests import run_astar_tests

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
    # run_astar_tests()



    # print("\n\n=BEAM SEARCH 6 SIMPLU=\n")
    # f = open("files/problems6.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]
    # print(manhattan_heuristic(problems[2]))
    # print(dist_Manhattan(problems[2]))
