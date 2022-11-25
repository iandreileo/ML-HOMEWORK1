import math
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *

    
B = [ 50, 100, 500, 1000]   

def run_beam_tests():

    # BEAM SEARCH EASY
    
    # Teste 6 EASY
    print("\n\n=BEAM SEARCH 6 EASY=\n")
    f = open("files/problems6-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        if problem_index == 4:

            for b in list(reversed(B)):
                print("---- p =", problem_index, "-----")
                print("---- b =", b, "-----")

                beam_search1 = beam_search(problems[problem_index], b, manhattan_heuristic, 1000000)
                print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

                # beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 1000000)
                # print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

                print("/---- b =", b, "-----\n")


    # Teste 5 EASY
    print("\n\n=BEAM SEARCH 5 EASY=\n")
    f = open("files/problems5-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):
            print("---- p =", problem_index, "-----")
            print("---- b =", b, "-----")

            beam_search1 = beam_search(problems[problem_index], b, manhattan_heuristic, 500000)
            print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

            # beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 500000)
            # print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

            print("/---- b =", b, "-----\n")


    # Teste 4 EASY
    print("\n\n=BEAM SEARCH 4 EASY=\n")
    f = open("files/problems4-easy.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):
            print("---- p =", problem_index, "-----")
            print("---- b =", b, "-----")

            beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 100000)
            print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

            beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 100000)
            print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

            print("/---- b =", b, "-----\n")

    # BEAM SEARCH SIMPLU

    # Teste 6 SIMPLU
    print("\n\n=BEAM SEARCH 6 SIMPLU=\n")
    f = open("files/problems6.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):
            print("---- p =", problem_index, "-----")
            print("---- b =", b, "-----")

            beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 1000000)
            print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

            beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 1000000)
            print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

            print("/---- b =", b, "-----\n")


    # Teste 5 SIMPLU
    print("\n\n=BEAM SEARCH 5 SIMPLU=\n")
    f = open("files/problems5.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):
            print("---- p =", problem_index, "-----")
            print("---- b =", b, "-----")

            beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 500000)
            print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

            beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 500000)
            print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

            print("/---- b =", b, "-----\n")



    # Teste 4 SIMPLU
    print("\n\n=BEAM SEARCH 4 SIMPLU=\n")
    f = open("files/problems4.txt", "r")

    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]

    for problem_index in range(len(problems)):

        for b in list(reversed(B)):
            print("---- p =", problem_index, "-----")
            print("---- b =", b, "-----")

            beam_search1 = beam_search(problems[problem_index], b, linear_conflicts, 100000)
            print(problem_index, "," ,"LINEAR", ",", b, ",", beam_search1)

            beam_search2 = beam_search(problems[problem_index], b, manhattan_heuristic, 100000)
            print(problem_index, "," ,"MANHATTAN",",", b, ",",  beam_search2)

            print("/---- b =", b, "-----\n")