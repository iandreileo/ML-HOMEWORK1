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
