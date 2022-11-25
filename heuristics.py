import math

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


def manhattan_heuristic_test(a, b):
    array_a = a
    array_b = b

    sum = 0

    for i in range(len(array_a)):
        if(type(array_a[i]) == str and type(array_b[i]) == str):
            sum = sum + abs(0)
        
        elif (type(array_a[i]) == str):
            sum = sum + abs(- array_b[i])

        elif (type(array_b[i]) == str):
            sum = sum + abs(array_a[i])
        else:
            sum = sum + abs(array_a[i] - array_b[i])

    # print(a.r, b.r, sum)


    return sum


def linear_conflicts(candidate):
    def count_conflicts(candidate_row, solved_row, size, ans=0):
        counts = [0 for x in range(size)]
        for i, tile_1 in enumerate(candidate_row):
            if tile_1 in solved_row and tile_1 != 0:
                solved_i = solved_row.index(tile_1)
                for j, tile_2 in enumerate(candidate_row):
                    if tile_2 in solved_row and tile_2 != 0 and i != j:
                        solved_j = solved_row.index(tile_2)
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

    size = int(math.sqrt(len(candidate.r)))
    solved = candidate.solved()

    res = manhattan_heuristic(candidate)
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
    for i in range(size):
        res += count_conflicts(candidate_rows[i], solved_rows[i], size)
    for i in range(size):
        res += count_conflicts(candidate_columns[i], solved_columns[i], size)
    return res