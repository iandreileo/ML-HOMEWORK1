import math
import copy
from schelet import NPuzzle

# Euristica pentru Manhattan
# Aplicam formula din laborator
def manhattan_heuristic(stare):
    # Setam suma ca fiind 0
    sum = 0

    # Calculam care este lungimea unui rand/coloane
    length = int(math.sqrt(len(stare.r)))

    for i in range(len(stare.r)):
        # Setam pozitia curenta
        current = stare.r[i]

        # Daca e diferita de caracterul spatiu, calculam pe ce pozitie ar fi trebuit sa fie defapt\
        # Raportat la lungimea unui rand/coloane
        if current != ' ':
            y_normal = (current - 1) // length
            if current % length == 0:
                x_normal = length - 1
            else:
                x_normal = current % length - 1
            
            # Folosim formula manhattan de calcul dintre 2 puncte
            sum += abs(i // length - y_normal) + abs (i % length - x_normal)

    return sum


# Euristica pentru Hamming
# Vedem cate pozitii sunt diferite
def hamming_heuristic(a):

    b = a.solved()

    if len(a.r) != len(b.r):
        return -1
    
    sum = 0

    for i in range(len(a.r)):
        if(a.r[i] != b.r[i]):
            sum+=1

    return sum

def count_conflicts(candidate_row, solved_row, size, ans=0):

    counts = [0 for x in range(size)]

    for i in range(len(candidate_row)):

        if candidate_row[i] in solved_row and candidate_row[i] != 0:

            solved_i = solved_row.index(candidate_row[i])

            for j in range(len(candidate_row)):

                if candidate_row[j] in solved_row and candidate_row[j] != 0 and i != j:

                    solved_j = solved_row.index(candidate_row[j])

                    if solved_i > solved_j and i < j:
                        counts[i] += 1

                    if solved_i < solved_j and i > j:
                        counts[i] += 1

    if max(counts) == 0:
        return ans * 2
    else:
        i = counts.index(max(counts))
        candidate_row[i] = -1
        ans += 1
        
        return count_conflicts(candidate_row, solved_row, size, ans)

def linear_conflicts(candidate):

    # Lungimea unei linii/coloane
    size = int(math.sqrt(len(candidate.r)))

    # Puzzle-ul rezolvat
    solved = candidate.solved()

    # Aplicam euristica manhattan
    res = manhattan_heuristic(candidate)

    # Initializam si incarcam
    # Starile initiale si cele rezolvate
    candidate_rows = [[] for y in range(size)]
    candidate_columns = [[] for x in range(size)]

    solved_rows = [[] for y in range(size)]
    solved_columns = [[] for x in range(size)]

    for y in range(size):
        for x in range(size):
            idx = (y * size) + x

            candidate_rows[y].append(candidate.r[idx])
            candidate_columns[x].append(candidate.r[idx])

            solved_rows[y].append(solved.r[idx])
            solved_columns[x].append(solved.r[idx])

    # Calculam recursiv conflictele
    # Pe coloane si randuri
    for i in range(size):
        res += count_conflicts(candidate_rows[i], solved_rows[i], size)
        res += count_conflicts(candidate_columns[i], solved_columns[i], size)

    return res

