from state import next_state, solved_state
import numpy as np
from location import next_location, solved_location
from queue import PriorityQueue

def heuristic(location):
    dict = {1 : [0, 0, 0], 2 : [0, 0, 1], 3 : [0, 1, 0], 4 : [0, 1, 1], 5: [1, 0, 0], 6: [1, 0, 1], 7: [1, 1, 0], 8: [1, 1, 1]}
    manhattan = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                manhattan+= np.sum(np.fabs(dict[location[i][j][k]] - np.array([i, j, k])))
    return manhattan / 4

def Astar(state, init_location):
    q = PriorityQueue()
    count = 0
    explore = 0
    expand = 0
    visited = {}
    visited[str(state)] = True
    q.put([heuristic(init_location), count, state, init_location, []])
    while not q.empty():
        # global explore
        explore += 1
        current = q.get()
        current_state = current[2]
        visited[str(current_state)] = True
        current_loc = current[3]
        if np.array_equal(current_state, solved_state()):
            return current[4]
        expand += 1
        for i in range(1, 13):
            next = next_state(current_state, i)
            if str(next) in visited:
                continue
            next_loc = next_location(current_loc, i)
            g = 1+len(current[4])
            h = heuristic(next_loc)
            count += 1
            q.put([g+h, count, next, next_loc, (current[4] + [i])])