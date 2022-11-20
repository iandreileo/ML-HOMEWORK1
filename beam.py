from astar import *
import functools


def beam_search(start, B, h, limita):
    success = False
    beam = {start}
    vizitat = {start}

    while len(beam) and len(vizitat) < limita:
        succ = []

        for s in beam:
            succ = succ + get_neighbours(s)

        # Daca o stare e finala
        # Returnam success
        for i in succ:
            if i.r == i.solved().r:
                return success
        
        selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]
        
        vizitat = vizitat.union(selectat)

        beam = set(selectat)

        # print("---------------\n" + str(beam) + "-----------------\n")
        
    return success