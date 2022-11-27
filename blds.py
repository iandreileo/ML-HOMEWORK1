

import copy
import time
from astar import get_neighbours

def Iter(nivel: dict, discrepante, B, h, vizitat, limita):
    succ = {}

    for s in nivel:
        neighbours = get_neighbours(s)

        for neigh in neighbours:
            if neigh.r == neigh.solved().r:
                return [len(vizitat), len(neigh.moves)]

            if (neigh not in vizitat) and (neigh is not None):
                succ[neigh] = h(neigh)


    if len(succ) == 0:
        return False

    if (len(vizitat) + min(B, len(succ))) > limita:
        return False

    succ = sorted(succ.items(), key=lambda item: item[1])

    if discrepante == 0:
        nivel_urm = dict(succ[:B])

        vizitat.update(nivel_urm)
        
        return Iter(nivel_urm, 0, B, h, vizitat, limita)

    else:
        deja_explorate = B
        while deja_explorate < len(succ):
            n = min(len(succ) - deja_explorate, B)

            nivel_urm = dict(succ[:deja_explorate][:n])

            vizitat.update(nivel_urm)

            val = Iter(nivel_urm, discrepante - 1, B, h,vizitat, limita )

            if val:
                return True

            deja_explorate = deja_explorate + len(nivel_urm)

        nivel_urm = dict(succ[:B])

        vizitat.update(nivel_urm)

        return Iter(nivel_urm, discrepante, B, h ,vizitat, limita)


def BLDS(start, h, B, limita):
    start_time = time.time()

    vizitat = {start: (h(start))}

    discrepante = 0

    while True:
        iter = Iter({start: (h(start))}, discrepante, B, h, vizitat, limita)

        current_time = time.time() -  start_time

        if iter:
            iter.insert(0, current_time)
            return iter
        
        discrepante = discrepante + 1