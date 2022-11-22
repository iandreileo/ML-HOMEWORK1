import math

# Euristica pentru Manhattan
# Aplicam formula din laborator
def manhattan_heuristic(a, b):
    array_a = a.r
    array_b = b.r

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

    return sum


# Euristica pentru Hamming
# Vedem cate pozitii sunt diferite
def hamming_heuristic(a,b):
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


def linear_conflicts(candidate, solved):
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

    res = manhattan_heuristic(candidate, solved)
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