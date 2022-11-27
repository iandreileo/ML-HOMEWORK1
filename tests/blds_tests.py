import math
from blds import BLDS
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *

    
B = [10, 50, 100, 500, 1000]   

def run_blds_tests():

    # BEAM SEARCH EASY
    
    # Teste 6 EASY
    # print("\n\n=BEAM SEARCH 6 EASY=\n")
    f = open("files/problems6-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 1000000)
            print("6" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 1000000)
            print("6" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))


    # Teste 5 EASY
    # print("\n\n=BEAM SEARCH 5 EASY=\n")
    f = open("files/problems5-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 500000)
            print("5" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 500000)
            print("5" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))

    # Teste 4 EASY
    # print("\n\n=BEAM SEARCH 4 EASY=\n")
    f = open("files/problems4-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 100000)
            print("4" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 100000)
            print("4" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))


    # NORMAL


    # Teste 6 SIMPLE
    # print("\n\n=BEAM SEARCH 6 SIMPLE=\n")
    f = open("files/problems6.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 1000000)
            print("6" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 1000000)
            print("6" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))


    # Teste 5 SIMPLE
    # print("\n\n=BEAM SEARCH 5 SIMPLE=\n")
    f = open("files/problems5.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 500000)
            print("5" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 500000)
            print("5" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))

    # Teste 4 SIMPLE
    # print("\n\n=BEAM SEARCH 4 SIMPLE=\n")
    f = open("files/problems4.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):

            blds1 = BLDS(problems[problem_index], linear_conflicts, b, 100000)
            print("4" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(blds1[0]) + "," + str(blds1[1]) + "," + str(blds1[2]) + "," + str(b))

            blds2 = BLDS(problems[problem_index], manhattan_heuristic, b, 100000)
            print("4" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(blds2[0]) + "," + str(blds2[1]) + "," + str(blds2[2]) + "," + str(b))


 