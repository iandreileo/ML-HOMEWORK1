import math
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *


if __name__ == '__main__':

    # f = open("files/problems4-easy.txt", "r")
    f = open("files/problems4 copy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]
    problems[0].display()

    # print(problems[0].r)

    astar = astar(problems[0], problems[0].solved(), manhattan_heuristic)

    print(astar)
