from astar import *
import functools
from heuristics import *


def beam_search(start, B, h, limita):
    success = False

    # 1. beam = {start}
    beam = []
    beam.append(start)

    # 2. vizitat = {start}
    vizitat = []
    vizitat.append(start)

    # 3. cat timp beam ̸= ∅ s, i |vizitat| < limita
    while len(beam) and len(vizitat) < limita:
        succ = []

        # 5. pentru fiecare s ∈ beam
        for s in beam:

            # 6. succ = succ ∪ succesori(s)
            current_neighbours = get_neighbours(s)
            for i in current_neighbours:
                if i not in vizitat:
                    succ.append(i)
                    
                    # 7. daca vreuna dintre dintre starile din succ este stare scop 
                    if i.r == i.solved().r:
                        return True

        # 9. selectat = cele mai bune B stari, sortate dupa h(s)
        if len(succ) < B:
            selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:len(succ)]
        
        else:
            selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]

        # 10. vizitat = vizitat ∪ selectat
        vizitat += selectat

        # 11. beam = selectat 
        beam = selectat
        
    return success