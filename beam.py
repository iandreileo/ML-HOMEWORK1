from astar import *
import functools
from heuristics import *
import time

MAX_EXECUTION_TIME = 60 * 2

def beam_search(start, B, h, limita):

    start_time = time.time()
    success = False

    # 1. beam = {start}
    beam = []
    # beam.add(start)
    beam += [start]

    # 2. vizitat = {start}
    vizitat = {start: (None)}

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
                        return (time.time() - start_time, len(vizitat), len(i.moves))

        # 9. selectat = cele mai bune B stari, sortate dupa h(s)
        if len(succ) < B:
            selectat = sorted(succ, key=lambda x: h(x))[0:len(succ)]
        
        else:
            selectat = sorted(succ, key=lambda x: h(x))[0:B]

        # 10. vizitat = vizitat ∪ selectat
        for i in selectat:
            vizitat[i] = (None)

        # 11. beam = selectat 
        beam = selectat

        # De sters   
        if((time.time() - start_time) > MAX_EXECUTION_TIME):
            return (time.time() - start_time, None)
        
    return (time.time() - start_time, len(vizitat), None)
