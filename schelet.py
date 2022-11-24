import random, math
from _functools import reduce
from copy import copy
# from builtins import isinstance
# from resource import setrlimit, RLIMIT_AS, RLIMIT_DATA
import time

B = [ 50, 100, 500, 1000]   

class NPuzzle:
	"""
	Reprezentarea unei stări a problemei și a istoriei mutărilor care au adus starea aici.
	
	Conține funcționalitate pentru
	- afișare
	- citirea unei stări dintr-o intrare pe o linie de text
	- obținerea sau ștergerea istoriei de mutări
	- obținerea variantei rezolvate a acestei probleme
	- verificarea dacă o listă de mutări fac ca această stare să devină rezolvată.
	"""

	NMOVES = 4
	UP, DOWN, LEFT, RIGHT = range(NMOVES)
	ACTIONS = [UP, DOWN, LEFT, RIGHT]
	names = "UP, DOWN, LEFT, RIGHT".split(", ")
	BLANK = ' '
	delta = dict(zip(ACTIONS, [(-1, 0), (1, 0), (0, -1), (0, 1)]))
	
	PAD = 2
	
	def __init__(self, puzzle : list[int | str], movesList : list[int] = []):
		"""
		Creează o stare nouă pe baza unei liste liniare de piese, care se copiază.
		
		Opțional, se poate copia și lista de mutări dată.
		"""
		self.N = len(puzzle)
		self.side = int(math.sqrt(self.N))
		self.r = copy(puzzle)
		self.moves = copy(movesList)
	
	def display(self, show = True) -> str:
		l = "-" * ((NPuzzle.PAD + 1) * self.side + 1)
		aslist = self.r
		
		slices = [aslist[ slice * self.side : (slice+1) * self.side ]  for slice in range(self.side)]
		s = ' |\n| '.join([' '.join([str(e).rjust(NPuzzle.PAD, ' ') for e in line]) for line in slices]) 
	
		s = ' ' + l + '\n| ' + s + ' |\n ' + l
		if show: print(s)
		return s
	def display_moves(self):
		print([names[a] if a is not None else None for a in moves])
		
	def print_line(self):
		return str(self.r)
	
	@staticmethod
	def read_from_line(line : str):
		list = line.strip('\n][').split(', ')
		numeric = [NPuzzle.BLANK if e == "' '" else int(e) for e in list]
		return NPuzzle(numeric)
	
	def clear_moves(self):
		"""Șterge istoria mutărilor pentru această stare."""
		self.moves.clear()
	
	def apply_move_inplace(self, move : int):
		"""Aplică o mutare, modificând această stare."""
		blankpos = self.r.index(NPuzzle.BLANK)
		y, x = blankpos // self.side, blankpos % self.side
		ny, nx = y + NPuzzle.delta[move][0], x + NPuzzle.delta[move][1]
		if ny < 0 or ny >= self.side or nx < 0 or nx >= self.side: return None
		newpos = ny * self.side + nx
		piece = self.r[newpos]
		self.r[blankpos] = piece
		self.r[newpos] = NPuzzle.BLANK
		self.moves.append(move)
		return self
	
	def apply_move(self, move : int):
		"""Construiește o nouă stare, rezultată în urma aplicării mutării date."""
		return self.clone().apply_move_inplace(move)

	def solved(self):
		"""Întoarce varianta rezolvată a unei probleme de aceeași dimensiune."""
		return NPuzzle(list(range(self.N))[1:] + [NPuzzle.BLANK])

	def verify_solved(self, moves : list[int]) -> bool:
		""""Verifică dacă aplicarea mutărilor date pe starea curentă duce la soluție"""
		return reduce(lambda s, m: s.apply_move_inplace(m), moves, self.clone()) == self.solved()

	def clone(self):
		return NPuzzle(self.r, self.moves)
	def __str__(self) -> str:
		return str(self.N-1) + "-puzzle:" + str(self.r)
	def __repr__(self) -> str: return str(self)
	def __eq__(self, other):
		return self.r == other.r
	def __lt__(self, other):
		return True
	def __hash__(self):
		return hash(tuple(self.r))
	

# def get_neighbours(pos):
#     # Setam vecinii
#     neighbours = []

#     for i in NPuzzle.ACTIONS:
#         if pos.apply_move(i):
#             neighbours.append(pos.apply_move(i))

#     return neighbours

# import math

# # Euristica pentru Manhattan
# # Aplicam formula din laborator
# def manhattan_heuristic(a, b):
#     array_a = a.r
#     array_b = b.r

#     sum = 0

#     for i in range(len(array_a)):
#         if(type(array_a[i]) == str and type(array_b[i]) == str):
#             sum = sum + abs(0)
        
#         elif (type(array_a[i]) == str):
#             sum = sum + abs(- array_b[i])

#         elif (type(array_b[i]) == str):
#             sum = sum + abs(array_a[i])
#         else:
#             sum = sum + abs(array_a[i] - array_b[i])

#     return sum


# # Euristica pentru Hamming
# # Vedem cate pozitii sunt diferite
# def hamming_heuristic(a,b):
#     if len(a.r) != len(b.r):
#         return -1
    
#     sum = 0

#     for i in range(len(a.r)):
#         if(a.r[i] != b.r[i]):
#             sum+=1

#     return sum


# def manhattan_heuristic_test(a, b):
#     array_a = a
#     array_b = b

#     sum = 0

#     for i in range(len(array_a)):
#         if(type(array_a[i]) == str and type(array_b[i]) == str):
#             sum = sum + abs(0)
        
#         elif (type(array_a[i]) == str):
#             sum = sum + abs(- array_b[i])

#         elif (type(array_b[i]) == str):
#             sum = sum + abs(array_a[i])
#         else:
#             sum = sum + abs(array_a[i] - array_b[i])

#     # print(a.r, b.r, sum)


#     return sum


# def linear_conflicts(candidate, solved):
#     def count_conflicts(candidate_row, solved_row, size, ans=0):
#         counts = [0 for x in range(size)]
#         for i, tile_1 in enumerate(candidate_row):
#             if tile_1 in solved_row and tile_1 != 0:
#                 solved_i = solved_row.index(tile_1)
#                 for j, tile_2 in enumerate(candidate_row):
#                     if tile_2 in solved_row and tile_2 != 0 and i != j:
#                         solved_j = solved_row.index(tile_2)
#                         if solved_i > solved_j and i < j:
#                             counts[i] += 1
#                         if solved_i < solved_j and i > j:
#                             counts[i] += 1
#         if max(counts) == 0:
#             return ans * 2
#         else:
#             i = counts.index(max(counts))
#             candidate_row[i] = -1
#             ans += 1
#             return count_conflicts(candidate_row, solved_row, size, ans)

#     size = int(math.sqrt(len(candidate.r)))

#     res = manhattan_heuristic(candidate, solved)
#     candidate_rows = [[] for y in range(size)]
#     candidate_columns = [[] for x in range(size)]
#     solved_rows = [[] for y in range(size)]
#     solved_columns = [[] for x in range(size)]
#     for y in range(size):
#         for x in range(size):
#             idx = (y * size) + x
#             candidate_rows[y].append(candidate.r[idx])
#             candidate_columns[x].append(candidate.r[idx])
#             solved_rows[y].append(solved.r[idx])
#             solved_columns[x].append(solved.r[idx])
#     for i in range(size):
#         res += count_conflicts(candidate_rows[i], solved_rows[i], size)
#     for i in range(size):
#         res += count_conflicts(candidate_columns[i], solved_columns[i], size)
#     return res

# MAX_EXECUTION_TIME = 60 * 2

# def beam_search(start, B, h, limita):

#     # start_time = time.time()
#     success = False

#     # 1. beam = {start}
#     beam = []
#     # beam.add(start)
#     beam += [start]

#     # 2. vizitat = {start}
#     vizitat = {start: (None)}

#     # 3. cat timp beam ̸= ∅ s, i |vizitat| < limita
#     while len(beam) and len(vizitat) < limita:
       
#         succ = set()

#         # 5. pentru fiecare s ∈ beam
#         for s in beam:

#             # De sters   
#             # if((time.time() - start_time) > MAX_EXECUTION_TIME):
#                 # return (time.time() - start_time, None)

#             # 6. succ = succ ∪ succesori(s)
#             current_neighbours = get_neighbours(s)
#             for i in current_neighbours:
#                 if (i is not None) and (i not in vizitat):
#                     succ.add(i)
                    
#                     # 7. daca vreuna dintre dintre starile din succ este stare scop 
#                     if i.r == i.solved().r:
#                         return True

#         # 9. selectat = cele mai bune B stari, sortate dupa h(s)
#         if len(succ) < B:
#             selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:len(succ)]
        
#         else:
#             selectat = sorted(succ, key=lambda x: h(x, x.solved()))[0:B]

#         # 10. vizitat = vizitat ∪ selectat
#         for i in selectat:
#             vizitat[i] = (None)

#         # print(len(vizitat))

#         # vizitat = vizitat.union(selectat)

#         # 11. beam = selectat 
#         beam = selectat

#         # De sters   
        
#     return False

#    # Teste 6 EASY
# f = open("files/problems4-easy.txt", "r")
# input = f.readlines()
# f.close()
# problems4e = [NPuzzle.read_from_line(line) for line in input]
# # val = BLDS(problems4[0].clone(), dist_Manhattan, 100, 5000)
# f = open("files/problems5-easy.txt", "r")
# input = f.readlines()
# f.close()
# problems5e = [NPuzzle.read_from_line(line) for line in input]

# f = open("files/problems6-easy.txt", "r")
# input = f.readlines()
# f.close()
# problems6e = [NPuzzle.read_from_line(line) for line in input]

# f = open("files/problems4.txt", "r")
# input = f.readlines()
# f.close()
# problems4 = [NPuzzle.read_from_line(line) for line in input]

# f = open("files/problems5.txt", "r")
# input = f.readlines()
# f.close()
# problems5 = [NPuzzle.read_from_line(line) for line in input]

# f = open("files/problems6.txt", "r")
# input = f.readlines()
# f.close()
# problems6 = [NPuzzle.read_from_line(line) for line in input]

# problems = [(problems4e, 100000), (problems5e, 500000), (problems6e, 1000000), (problems4, 100000), (problems5, 500000), (problems6, 1000000)]

# B_val = [1, 10, 50, 100, 500, 1000]

# t_start = time.time()


# print("BEAM")
# for problem, limit in problems:
# 	print("____________________________________")
# 	for i in range(5):
# 		for B in B_val:
# 			t_s = time.time()
# 			val = beam_search(problem[i].clone(), B, manhattan_heuristic, limit)
# 			t_f = time.time()
# 			print(i, B, val)
