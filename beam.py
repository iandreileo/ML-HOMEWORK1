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
    beam += [start]

    # 2. vizitat = {start}
    vizitat = []
    vizitat += [start]

    # 3. cat timp beam ̸= ∅ s, i |vizitat| < limita
    while len(beam) and len(vizitat) < limita:
       
        succ = []

        # 5. pentru fiecare s ∈ beam
        for s in beam:

            # De sters   
            if((time.time() - start_time) > MAX_EXECUTION_TIME):
                return (time.time() - start_time, None)

            # 6. succ = succ ∪ succesori(s)
            current_neighbours = get_neighbours(s)
            for i in current_neighbours:
                if (i is not None) and (i not in vizitat):
                    succ.append(i)
                    
                    # 7. daca vreuna dintre dintre starile din succ este stare scop 
                    if i.r == i.solved().r:
                        return (time.time() - start_time, True)

        # 9. selectat = cele mai bune B stari, sortate dupa h(s)
        # if len(succ) < B:
        #     selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:len(succ)]
        
        # else:
        #     selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]

        # De testat daca sorteaza bine
        selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]


        # 10. vizitat = vizitat ∪ selectat
        vizitat = vizitat + selectat

        # 11. beam = selectat 
        beam = selectat

        # De sters   
        if((time.time() - start_time) > MAX_EXECUTION_TIME):
            return (time.time() - start_time, None)
        
    return (time.time() - start_time, False)
