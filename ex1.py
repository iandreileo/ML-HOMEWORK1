import math
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *

if __name__ == '__main__':

    f = open("files/problems4-easy.txt", "r")
    # f = open("files/problems4 copy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]
    problem = problems[1]
    problem.display()

    astar = astar(problem, problem.solved(), manhattan_heuristic)
    print(astar)
