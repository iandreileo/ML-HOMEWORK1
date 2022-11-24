from astar import *
import functools
from heuristics import *
import time

MAX_EXECUTION_TIME = 60 * 2

def beam_search(start, B, h, limita):

    start_time = time.time()
    success = False

    # 1. beam = {start}
    beam = set()
    beam.add(start)
    # beam += [start]

    # 2. vizitat = {start}
    vizitat = set()
    vizitat.add(start)

    # 3. cat timp beam ̸= ∅ s, i |vizitat| < limita
    while len(beam) and len(vizitat) < limita:
       
        succ = set()

        # 5. pentru fiecare s ∈ beam
        for s in beam:

            # De sters   
            if((time.time() - start_time) > MAX_EXECUTION_TIME):
                return (time.time() - start_time, None)

            # 6. succ = succ ∪ succesori(s)
            current_neighbours = get_neighbours(s)
            for i in current_neighbours:
                if (i is not None) and (i not in vizitat):
                    succ.add(i)
                    
                    # 7. daca vreuna dintre dintre starile din succ este stare scop 
                    if i.r == i.solved().r:
                        return (time.time() - start_time, True)

        # 9. selectat = cele mai bune B stari, sortate dupa h(s)
        if len(succ) < B:
            selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:len(succ)]
        
        else:
            selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]

        # print("\n\n")
        # for i in selectat:
        #     print(i, h(i, i.solved()))
        # print("\n\n")

        # 10. vizitat = vizitat ∪ selectat
        vizitat = vizitat.union(set(selectat))

        # 11. beam = selectat 
        beam = selectat

        # De sters   
        if((time.time() - start_time) > MAX_EXECUTION_TIME):
            return (time.time() - start_time, None)
        
    return (time.time() - start_time, False)
