import math
from glds import GLDS
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *

    
B = [1, 10, 50, 100, 500, 1000]   

def run_glds_tests():
    
    # Teste 6 EASY
    f = open("files/problems4-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        # glds1 = GLDS(problems[problem_index], linear_conflicts, 500000)
        # print("6" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(glds1[0]) + "," + str(glds1[1]) + "," + str(glds1[2]))

        glds2 = GLDS(problems[problem_index].clone(), manhattan_heuristic, 100000)
        print("6"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN""," + str(glds2[0]) + "," + str(glds2[1]) + "," + str(glds2[2]))



