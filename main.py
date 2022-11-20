import math
from heuristics import *
from heapq import heappop, heappush
import copy

from schelet import NPuzzle

def is_good(pos):
    return

def get_neighbors(pos):
    return

# def get_neighbour(pos):


def get_neighbours(pos):
    # Setam vecinii
    neighbours = []

    for i in range(4):
        if pos.apply_move(i):
            neighbours.append(pos.apply_move(i))

    return neighbours

def a_star_algorithm(start, end, heuristic):
    return

def astar(start, end, h):
    # Frontiera, ca listă (heap) de tupluri (cost-total-estimat, nod)
    frontier = []
    
    heappush(frontier, (0 + h(start, end), start))
        
    # Nodurile descoperite ca dicționar nod -> (părinte, cost-până-la-nod)
    discovered = {start: (None, 0)}    

    # print(discovered)
    
    # Marim frontiera
    while frontier:
        # Scoatem boardul curent
        s = heappop(frontier)

        # Splutim board si cost
        (cost,node) = s

        # print(node.apply_move(4))
        print(get_neighbours(node))

        # Testam daca s-a terminat
        if node.r == end.r:
            break

        # Mergem prin vecini
        for v_node in get_neighbours(node):
            print(v_node)
            

            


    #     if node == end:
    #         break
    #     for v_node in get_neighbours(node):
    #         if is_good(v_node):
    #             v_cost = discovered[node][1] + 1
    #             if v_node not in discovered:
    #                 heappush(frontier, (v_cost + h(v_node,end) , v_node))
    #                 discovered[v_node] = (node,v_cost)
    #             else:
    #                 (v_node_already, v_cost_already_in_discovered) = discovered[v_node]
    #                 if v_cost < v_cost_already_in_discovered :
    #                     heappush(frontier, (v_cost + h(v_node,end) , v_node))
    #                     discovered[v_node] = (node,v_cost)

    # cost_map = [[discovered[(r,c)][1] if (r,c) in discovered else 0 for c in range(math.sqrt(len(start)))]for r in range(math.sqrt(len(start)))]
    
    # # Refacem drumul
    # path = []
    # node = discovered[end][0]
    # while node is not None:
    #     path.insert(0, node)
    #     node = discovered[node][0]
        
    # return path # drumul, ca listă de poziții

if __name__ == '__main__':
    # print(manhattan_heuristic((2,3), (4,0)))
    # print(hamming_heuristic((4,3), (4,0)))

    f = open("files/problems4.txt", "r")
    input = f.readlines()
    f.close()
    problems = [NPuzzle.read_from_line(line) for line in input]
    problems[0].display()


    inputt = [11, 3, 2, 4, 1, 9, 14, 10, 13, 8, ' ', 12, 15, 5, 6, 7]

    print(problems[0].r)

    print(astar(problems[0], problems[0].solved(), hamming_heuristic))