# Euristica pentru Manhattan
# Aplicam formula din laborator
def manhattan_heuristic(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a.r,b.r))


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