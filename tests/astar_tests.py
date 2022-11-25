import math
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *

    
B = [ 1, 10, 50, 100, 500, 1000]   

def run_astar_tests():

    # ASTAR SEARCH EASY
    
    # Teste 6 EASY
    # print("\n\n=ASTAR 6 EASY=\n")
    f = open("files/problems6-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):
        # print("---- p =", problem_index, "-----")

        astar1 = astar(problems[problem_index], problems[problem_index].solved(), linear_conflicts)
        print("6" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(astar1[0]) + "," + str(astar1[1]) + "," + str(astar1[2]))

        astar2 = astar(problems[problem_index], problems[problem_index].solved(), manhattan_heuristic)
        # print(str(problem_index) + "," + "EASY" + "," + "MANHATTAN" + "," + str(astar2[0]) + "," + str(astar2[1]) + "," + str(astar2[2]))
        print("6"+  ","  + "EASY" +  ","+ str(problem_index) + "," + "MANHATTAN" + "," + str(astar2[0]) + "," + str(astar2[1]) + "," + str(astar2[2]))

        # print("/---- p =", problem_index, "-----\n")


    # Teste 5 EASY
    # print("\n\n=ASTAR 5 EASY=\n")
    f = open("files/problems5-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):
        # print("---- p =", problem_index, "-----")

        astar1 = astar(problems[problem_index], problems[problem_index].solved(), linear_conflicts)
        print("5" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(astar1[0]) + "," + str(astar1[1]) + "," + str(astar1[2]))

        astar2 = astar(problems[problem_index], problems[problem_index].solved(), manhattan_heuristic)
        print("5"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(astar2[0]) + "," + str(astar2[1]) + "," + str(astar2[2]))

        # print("/---- p =", problem_index, "-----\n")


    # Teste 4 EASY
    # print("\n\n=ASTAR 4 EASY=\n")
    f = open("files/problems4-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):
        # print("---- p =", problem_index, "-----")

        astar1 = astar(problems[problem_index], problems[problem_index].solved(), linear_conflicts)
        print("4" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(astar1[0]) + "," + str(astar1[1]) + "," + str(astar1[2]))

        astar2 = astar(problems[problem_index], problems[problem_index].solved(), manhattan_heuristic)
        print("4"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(astar2[0]) + "," + str(astar2[1]) + "," + str(astar2[2]))

        # print("/---- p =", problem_index, "-----\n")
