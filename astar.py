from heapq import heappop, heappush


def get_neighbours(pos):
    # Setam vecinii
    neighbours = []

    for i in range(4):
        if pos.apply_move(i):
            neighbours.append(pos.apply_move(i))

    return neighbours


def astar(start, end, h):
    # Frontiera, ca listă (heap) de tupluri (cost-total-estimat, nod)
    frontier = []
    
    heappush(frontier, (0 + h(start, end), start))
        
    # Nodurile descoperite ca dicționar nod -> (părinte, cost-până-la-nod)
    discovered = {start: (None, 0)}    
    
    # Marim frontiera
    while frontier:
        # Scoatem boardul curent
        s = heappop(frontier)

        # Splutim board si cost
        (cost,node) = s

        # 
        cost_pana_nod = discovered[node][1]

        # Testam daca s-a terminat
        if node.r == end.r:
            break

        # Mergem prin vecini
        for v_node in get_neighbours(node):
            cost_pana_la_vecin = cost_pana_nod + 1

            if v_node not in discovered or cost_pana_la_vecin < discovered[v_node][1]:
                discovered[v_node] = (node, cost_pana_la_vecin)
                heappush(frontier, (cost_pana_la_vecin + h(v_node, end), v_node))
            

    path = []
    current_node = end
    while current_node:
        path.append(current_node)
        current_node = discovered[current_node][0]

    return path