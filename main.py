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

    # print(problems[0].r)

    # astar = astar(problem, problem.solved(), manhattan_heuristic)

    # print(astar)

    beam = beam_search(problem, 50, manhattan_heuristic, 100000)
    print(beam)

    print(manhattan_heuristic_test([1, ' ', 2, 4, 3, 5, 10, 6, 8, 12, 11, 14, 9, 13, 15, 7], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']))
    print(manhattan_heuristic_test([1, ' ', 2, 4, 3, 5, 10, 6, 8, 12, 11, 14, 9, 13, 15, 7], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']))
    print(manhattan_heuristic_test([1, ' ', 2, 4, 3, 5, 10, 6, 8, 12, 11, 14, 9, 13, 15, 7], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']))
    print(manhattan_heuristic_test([1, ' ', 2, 4, 3, 5, 10, 6, 8, 12, 11, 14, 9, 13, 15, 7], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']))
    print(manhattan_heuristic_test([1, ' ', 2, 4, 3, 5, 10, 6, 8, 12, 11, 14, 9, 13, 15, 7], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,' ']))