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
    # print("\n\n=BEAM SEARCH 6 EASY=\n")
    f = open("files/problems4-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        glds1 = GLDS(problems[problem_index], linear_conflicts, 1000000)
        print("6" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(glds1[0]) + "," + str(glds1[1]) + "," + str(glds1[2]))

        glds2 = GLDS(problems[problem_index], manhattan_heuristic, 1000000)
        print("6"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(glds2[0]) + "," + str(glds2[1]) + "," + str(glds2[2]))



    # # Teste 5 EASY
    # # print("\n\n=BEAM SEARCH 5 EASY=\n")
    # f = open("files/problems5-easy.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]

    # for problem_index in range(len(problems)):

    #     for b in list(reversed(B)):

    #         beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 500000)
    #         print("5" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(beam_search1[0]) + "," + str(beam_search1[1]) + "," + str(beam_search1[2]) + "," + str(b))

    #         beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 500000)
    #         print("5"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(beam_search2[0]) + "," + str(beam_search2[1]) + "," + str(beam_search2[2])  + "," +str(b))



    # # Teste 4 EASY
    # # print("\n\n=BEAM SEARCH 4 EASY=\n")
    # f = open("files/problems4-easy.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]

    # for problem_index in range(len(problems)):

    #     for b in list(reversed(B)):
    #         beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 100000)
    #         print("4" +  ","  +  "EASY"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(beam_search1[0]) + "," + str(beam_search1[1]) + "," + str(beam_search1[2]) + "," + str(b))

    #         beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 100000)
    #         print("4"+  ","  + "EASY"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(beam_search2[0]) + "," + str(beam_search2[1]) + "," + str(beam_search2[2])  + "," +str(b))


    # # BEAM SEARCH SIMPLU

    # # Teste 6 SIMPLU
    # # print("\n\n=BEAM SEARCH 6 SIMPLU=\n")
    # f = open("files/problems6.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]

    # for problem_index in range(len(problems)):

    #     for b in list(reversed(B)):
    #         beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 1000000)
    #         print("6" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(beam_search1[0]) + "," + str(beam_search1[1]) + "," + str(beam_search1[2]) + "," + str(b))

    #         beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 1000000)
    #         print("6"+  ","  + "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(beam_search2[0]) + "," + str(beam_search2[1]) + "," + str(beam_search2[2])  + "," +str(b))


    # # Teste 5 SIMPLU
    # # print("\n\n=BEAM SEARCH 5 SIMPLU=\n")
    # f = open("files/problems5.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]

    # for problem_index in range(len(problems)):

    #     for b in list(reversed(B)):
    #         beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 500000)
    #         print("5" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(beam_search1[0]) + "," + str(beam_search1[1]) + "," + str(beam_search1[2]) + "," + str(b))

    #         beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 500000)
    #         print("5"+  ","  + "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(beam_search2[0]) + "," + str(beam_search2[1]) + "," + str(beam_search2[2])  + "," +str(b))



    # # Teste 4 SIMPLU
    # print("\n\n=BEAM SEARCH 4 SIMPLU=\n")
    # f = open("files/problems4.txt", "r")

    # input = f.readlines()
    # f.close()
    # problems = [NPuzzle.read_from_line(line) for line in input]

    # for problem_index in range(len(problems)):

    #     for b in list(reversed(B)):
    #         beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 100000)
    #         print("4" +  ","  +  "SIMPLE"+  "," + str(problem_index) + "," + "LINEAR" + "," + str(beam_search1[0]) + "," + str(beam_search1[1]) + "," + str(beam_search1[2]) + "," + str(b))

    #         beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 100000)
    #         print("4"+  ","  + "SIMPLE"+  "," + str(problem_index) + "," + "MANHATTAN" + "," + str(beam_search2[0]) + "," + str(beam_search2[1]) + "," + str(beam_search2[2])  + "," +str(b))
