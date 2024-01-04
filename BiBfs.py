from collections import deque
import time

def bidirectional_bfs(graph, start, end):
    if start == end:
        return [start], None

    queue_start = deque([(start, [start])])
    queue_end = deque([(end, [end])])

    visited_start = set([start])
    visited_end = set([end])

    visited_start.add(start)
    visited_start.add(end)


    while queue_start and queue_end:
        node_start, path_start = queue_start.popleft()
        neighbors_start = graph[node_start]

        for neighbor in neighbors_start:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                new_path_start = path_start + [neighbor]
                queue_start.append((neighbor, new_path_start))

                if neighbor in visited_end:
                    intersection = neighbor
                    path_end = get_path_end(neighbor, queue_end)
                    return new_path_start, path_end[1:]



        node_end, path_end = queue_end.popleft()
        neighbors_end = graph[node_end]


        for neighbor in neighbors_end:
            if neighbor not in visited_end:
                visited_end.add(neighbor)
                neighbor_list = [list(inner_tuple) for inner_tuple in neighbor]
                check = 0
                if neighbor_list[-1][0] == 1 and check == 0:
                    neighbor_list[-1][0] = 7
                    check = 1
                if neighbor_list[-1][0] == 2 and check == 0:
                    neighbor_list[-1][0] = 8
                    check = 1
                if neighbor_list[-1][0] == 3 and check == 0:
                    check = 1
                    neighbor_list[-1][0] = 9
                if neighbor_list[-1][0] == 4 and check == 0:
                    neighbor_list[-1][0] = 10
                    check = 1
                if neighbor_list[-1][0] == 5 and check == 0:
                    neighbor_list[-1][0] = 11
                    check = 1
                if neighbor_list[-1][0] == 6 and check == 0:
                    neighbor_list[-1][0] = 12
                    check = 1
                if neighbor_list[-1][0] == 7 and check == 0:
                    neighbor_list[-1][0] = 1
                    check = 1
                if neighbor_list[-1][0] == 8 and check == 0:
                    neighbor_list[-1][0] = 2
                    check = 1
                if neighbor_list[-1][0] == 9 and check == 0:
                    neighbor_list[-1][0] = 3
                    check = 1
                if neighbor_list[-1][0] == 10 and check == 0:
                    neighbor_list[-1][0] = 4
                    check = 1
                if neighbor_list[-1][0] == 11 and check == 0:
                    neighbor_list[-1][0] = 5
                    check = 1
                if neighbor_list[-1][0] == 12 and check == 0:
                    neighbor_list[-1][0] = 6
                    check = 1
                neighbor1 = tuple(tuple(inner_list) for inner_list in neighbor_list)
                new_path_end = [neighbor1] + path_end
                queue_end.append((neighbor, new_path_end))

                if neighbor in visited_start:
                    intersection = neighbor
                    path_start = get_path_start(neighbor, queue_start)
                    return path_start, new_path_end[1:]



    return None, None

def get_path_start(intersection, queue):
    for node, path in queue:
        if node == intersection:
            return path

def get_path_end(intersection, queue):
    for node, path in queue:
        if node == intersection:
            return path








