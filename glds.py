import math
from heuristics import *
from heapq import heappop, heappush
import copy
from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
from schelet import NPuzzle
from astar import *
from beam import *
import sys
import time
import resource

sys.setrecursionlimit(10 ** 7)

def Iteratie(stare, discrepante, h, vizitat, limita):
    succ = {}

    # 2. pentru fiecare s succesor al lui stare
    neighbours = get_neighbours(stare)

    for s in neighbours:
        # 3. daca s este stare scop atunci ıntoarce SUCCES
        if s.r == s.solved().r:
            return True

        # 4. daca s /∈ vizitat atunci succ = succ ∪ {s}
        if (s is not None) and (s not in vizitat):
            succ[s] = h(s)
    
    # 5. daca succ = ∅ atunci ıntoarce ESEC
    if len(succ) == 0:
        return False

    # 6. daca |vizitat| > limita atunci ıntoarce ESEC
    if len(vizitat) > limita:
        return False
    
    # 7. best = cea mai buna stare din succ, dupa h(s)
    best = sorted(succ.items(), key=lambda item: item[1])[0][0]

    # 8. daca discrepante = 0 atunci
    if discrepante == 0:
        # 9. ıntoarce Iteratie(best, 0, h, vizitat ∪ {best}, limita)
        vizitat_cu_best = copy.deepcopy(vizitat)
        vizitat_cu_best[best] = (succ[best])

        return Iteratie(best, 0, h, vizitat_cu_best, limita)

    else:
        # 11. succ = succ \ {best}
        succ.pop(best)

        # 12. cat timp succ ̸= ∅
        while len(succ):

            # 13. s = cea mai buna stare din succ, dupa h(s)
            s = sorted(succ.items(), key=lambda item: item[1])[0][0]

            # 15. daca Iteratie(s, discrepante − 1, h, vizitat ∪ {s}, limita) ıntoarce SUCCES
            vizitat_cu_s = copy.deepcopy(vizitat)
            vizitat_cu_s[s] = (succ[s])

            # 14. succ = succ \ {s}
            succ.pop(s)

            if Iteratie(s, discrepante - 1, h, vizitat_cu_s, limita):
                return True

        # 17. ıntoarce Iteratie(best, discrepante, h, vizitat ∪ {best}, limita)
        
        vizitat_cu_best = copy.deepcopy(vizitat)
        # print(succ)
        vizitat_cu_best[best] = (h(best))

        return Iteratie(best, discrepante, h, vizitat_cu_best, limita)

    

def GLDS(start, h, limita):
    start_time = time.time()

    # vizitat = {start}
    vizitat = {start: (h(start))}

    # discrepante = 0
    discrepante = 0

    # cat timp adevarat
    while True:

        # daca Iteratie(start, discrepante, h, vizitat, limita) ıntoarce SUCCES
        if Iteratie(stare = start, discrepante=discrepante, h=h, vizitat=copy.deepcopy(vizitat), limita=limita):
            return (time.time() - start_time, len(vizitat), vizitat)
        
        # discrepante = discrepante + 1
        discrepante = discrepante + 1