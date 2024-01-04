import numpy as np
from state import next_state, solved_state
from BiBfs import bidirectional_bfs
from astart import custom_a_star
import time


expand = 0
explor = 0


def dfs_with_max_depth(graph, start, target, max_depth,current_depth=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start[-1][0])

    startt = start[:-1]

    if startt == target:
        return path

    if current_depth >= max_depth:
        path.pop()
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_with_max_depth(graph, neighbor, target, max_depth, current_depth + 1, visited, path)
            if new_path:
                return new_path

    path.pop()

    return None

def addTograph(graph):
    global expand
    global explor
    empty = []
    for n in graph:
        if graph[n] == []:
            empty.append(n)
    for e in empty:
        expand += 1
        m = e[:-1]
        li = [list(map(int, tpl)) for tpl in m]
        first = tuple(map(tuple, next_state(li, 1)))
        a = (1, 1)
        first = first + (a, )
        if first not in graph:
            explor += 1
            graph[first] = []
            graph[e].append(first)


        second = tuple(map(tuple, next_state(li, 2)))
        b = (2, 2)
        second = second + (b,)
        if second not in graph:
            explor += 1
            graph[second] = []
            graph[e].append(second)


        third = tuple(map(tuple, next_state(li, 3)))
        c = (3, 3)
        third = third + (c, )
        if third not in graph:
            explor += 1
            graph[third] = []
            graph[e].append(third)


        forth = tuple(map(tuple, next_state(li, 4)))
        d = (4, 4)
        forth = forth + (d,)
        if forth not in graph:
            explor += 1
            graph[forth] = []
            graph[e].append(forth)

        fifith = tuple(map(tuple, next_state(li, 5)))
        f = (5, 5)
        fifith = fifith + (f,)
        if fifith not in graph:
            explor += 1
            graph[fifith] = []
            graph[e].append(fifith)

        sixth = tuple(map(tuple, next_state(li, 6)))
        g = (6, 6)
        sixth = sixth + (g,)
        if sixth not in graph:
            explor += 1
            graph[sixth] = []
            graph[e].append(sixth)


        seventh = tuple(map(tuple, next_state(li, 7)))
        h = (7, 7)
        seventh = seventh + (h,)
        if seventh not in graph:
            explor += 1
            graph[seventh] = []
            graph[e].append(seventh)

        eighth = tuple(map(tuple, next_state(li, 8)))
        i = (8, 8)
        eighth = eighth + (i,)
        if eighth not in graph:
            explor += 1
            graph[eighth] = []
            graph[e].append(eighth)


        ninth = tuple(map(tuple, next_state(li, 9)))
        j = (9, 9)
        ninth = ninth + (j,)
        if ninth not in graph:
            explor += 1
            graph[ninth] = []
            graph[e].append(ninth)

        tenth = tuple(map(tuple, next_state(li, 10)))
        k = (10, 10)
        tenth = tenth + (k,)
        if tenth not in graph:
            explor += 1
            graph[tenth] = []
            graph[e].append(tenth)


        eleventh = tuple(map(tuple, next_state(li, 11)))
        l = (11, 11)
        eleventh = eleventh + (l,)
        if eleventh not in graph:
            explor += 1
            graph[eleventh] = []
            graph[e].append(eleventh)

        twelevth = tuple(map(tuple, next_state(li, 12)))
        m = (12, 12)
        twelevth = twelevth + (m,)
        if twelevth not in graph:
            explor += 1
            graph[twelevth] = []
            graph[e].append(twelevth)
    return graph



def addTograph2(graph):
    empty = []
    global expand
    global explor
    for n in graph:
        if graph[n] == []:
            empty.append(n)
    for e in empty:
        expand += 1
        m = e[:-1]
        li = [list(map(int, tpl)) for tpl in m]
        first = tuple(map(tuple, next_state(li, 1)))
        a = (1, 1)
        first = first + (a, )
        if first not in graph:
            explor+= 1
            graph[first] = []
        graph[e].append(first)


        second = tuple(map(tuple, next_state(li, 2)))
        b = (2, 2)
        second = second + (b,)
        if second not in graph:
            explor += 1
            graph[second] = []
        graph[e].append(second)


        third = tuple(map(tuple, next_state(li, 3)))
        c = (3, 3)
        third = third + (c, )
        if third not in graph:
            explor += 1
            graph[third] = []
        graph[e].append(third)


        forth = tuple(map(tuple, next_state(li, 4)))
        d = (4, 4)
        forth = forth + (d,)
        if forth not in graph:
            explor += 1
            graph[forth] = []
        graph[e].append(forth)

        fifith = tuple(map(tuple, next_state(li, 5)))
        f = (5, 5)
        fifith = fifith + (f,)
        if fifith not in graph:
            explor += 1
            graph[fifith] = []
        graph[e].append(fifith)

        sixth = tuple(map(tuple, next_state(li, 6)))
        g = (6, 6)
        sixth = sixth + (g,)
        if sixth not in graph:
            explor += 1
            graph[sixth] = []
        graph[e].append(sixth)


        seventh = tuple(map(tuple, next_state(li, 7)))
        h = (7, 7)
        seventh = seventh + (h,)
        if seventh not in graph:
            explor += 1
            graph[seventh] = []
        graph[e].append(seventh)

        eighth = tuple(map(tuple, next_state(li, 8)))
        i = (8, 8)
        eighth = eighth + (i,)
        if eighth not in graph:
            explor += 1
            graph[eighth] = []
        graph[e].append(eighth)


        ninth = tuple(map(tuple, next_state(li, 9)))
        j = (9, 9)
        ninth = ninth + (j,)
        if ninth not in graph:
            explor += 1
            graph[ninth] = []
        graph[e].append(ninth)

        tenth = tuple(map(tuple, next_state(li, 10)))
        k = (10, 10)
        tenth = tenth + (k,)
        if tenth not in graph:
            explor += 1
            graph[tenth] = []
        graph[e].append(tenth)


        eleventh = tuple(map(tuple, next_state(li, 11)))
        l = (11, 11)
        eleventh = eleventh + (l,)
        if eleventh not in graph:
            explor += 1
            graph[eleventh] = []
        graph[e].append(eleventh)

        twelevth = tuple(map(tuple, next_state(li, 12)))
        m = (12, 12)
        twelevth = twelevth + (m,)
        if twelevth not in graph:
            explor += 1
            graph[twelevth] = []
        graph[e].append(twelevth)
    return graph




def solve(init_state, init_location, method, init=None):


    # instructions and hints:
    # 1. use 'solved_state()' to obtain the goal state.
    # 2. use 'next_state()' to obtain the next state when taking an action .
    # 3. use 'next_location()' to obtain the next location of the little cubes when taking an action.
    # 4. you can use 'Set', 'Dictionary', 'OrderedDict', and 'heapq' as efficient data structures.
    first_graph = {}
    deep = 1
    final_state = ((1, 1), (1, 1), (2, 2), (2, 2), (3, 3), (3, 3), (4, 4), (4, 4), (5, 5), (5, 5), (6, 6), (6, 6))
    if method == 'Random':
        return list(np.random.randint(1, 12+1, 10))
    
    elif method == 'IDS-DFS':
        init = tuple(map(tuple, init_state))
        ta = (0, 0)
        init = init + (ta, )
        first_graph[init] = []
        while True:
            first_graph = addTograph(first_graph)
            result = dfs_with_max_depth(first_graph, init, final_state, deep)
            if result:
                result = result[1:]
                print(f"explor :{explor}")
                print(f"expand :{expand}")
                print(f"deep : {deep}")
                return result
            else:
                deep += 1


    elif method == 'A*':
        result = custom_a_star(init_state, init_location)
        return result

    elif method == 'BiBFS':
        start_time = time.time()
        seconde_graph = {}
        init = tuple(map(tuple, init_state))
        ta = (0, 0)
        init = init + (ta,)
        final_state  = final_state + (ta, )
        seconde_graph[init] = []
        seconde_graph[final_state] = []
        while True:
            seconde_graph = addTograph2(seconde_graph)
            forward, backward= bidirectional_bfs(seconde_graph, init, final_state)
            if forward and backward:
                end_time = time.time()
                f_action = []
                b_action = []
                for r in forward:
                    if r[-1][0] != 0:
                        f_action.append(r[-1][0])
                for r in backward:
                    if r[-1][0] != 0:
                        b_action.append(r[-1][0])
                f_action.pop()
                print(f"explor :{explor}")
                print(f"expand :{expand}")
                print(f"time: {end_time - start_time}")
                print(f"deep : {deep}")
                return f_action + b_action
            else:
                deep += 1


    
    else:
        return []