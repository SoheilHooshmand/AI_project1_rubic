from state import next_state, solved_state
import numpy as np
from location import next_location, solved_location
from queue import PriorityQueue

def custom_heuristic(loc):
    mapping = {1: [0, 0, 0], 2: [0, 0, 1], 3: [0, 1, 0], 4: [0, 1, 1], 5: [1, 0, 0], 6: [1, 0, 1], 7: [1, 1, 0], 8: [1, 1, 1]}
    manhattan_dist = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                manhattan_dist += np.sum(np.fabs(mapping[loc[i][j][k]] - np.array([i, j, k])))
    return manhattan_dist / 4



def custom_a_star(init_state, init_loc):

    q = PriorityQueue()
    count = 0
    explore_count = 0
    expand_count = 0
    deep = 0
    visited_states = {}
    visited_states[str(init_state)] = True
    q.put([custom_heuristic(init_loc), count, init_state, init_loc, []])

    while not q.empty():
        explore_count += 1
        current = q.get()
        current_state = current[2]
        visited_states[str(current_state)] = True
        current_location = current[3]

        if np.array_equal(current_state, solved_state()):
            print(f"explor: {explore_count}")
            print(f"exapand: {expand_count}")
            print(f"deep: {deep}")
            return current[4]

        expand_count += 1
        for i in range(1, 13):
            next_state_val = next_state(current_state, i)

            if str(next_state_val) in visited_states:
                continue

            next_location_val = next_location(current_location, i)
            g_val = 1 + len(current[4])
            h_val = custom_heuristic(next_location_val)
            count += 1
            q.put([g_val + h_val, count, next_state_val, next_location_val, (current[4] + [i])])
        deep += 1

