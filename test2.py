from collections import deque

def bibfs(graph, start, target):
    if start == target:
        return [start]

    # Initialize forward and backward queues
    forward_queue = deque([(start, [start])])
    backward_queue = deque([(target, [target])])

    # Initialize visited sets for forward and backward searches
    forward_visited = set([start])
    backward_visited = set([target])

    while forward_queue and backward_queue:
        # Perform forward BFS
        current_forward, path_forward = forward_queue.popleft()
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append((neighbor, path_forward + [neighbor]))

                # Check if we meet in the middle
                if neighbor in backward_visited:
                    intersection_node = neighbor
                    forward_path = path_forward + [intersection_node]
                    backward_path = list(reversed(path_backward))
                    return forward_path + backward_path

        # Perform backward BFS
        current_backward, path_backward = backward_queue.popleft()
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append((neighbor, path_backward + [neighbor]))

                # Check if we meet in the middle
                if neighbor in forward_visited:
                    intersection_node = neighbor
                    forward_path = path_forward + [intersection_node]
                    backward_path = list(reversed(path_backward))
                    return forward_path + backward_path

    # If no path is found
    return None

# Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['B'],
#     'F': ['C'],
#     'G': ['C']
# }
#
# start_node = 'A'
# target_node = 'G'
#
# result = bibfs(graph, start_node, target_node)
#
# if result:
#     print(f"BiBFS path from {start_node} to {target_node}: {result}")
# else:
#     print(f"No path found from {start_node} to {target_node}")
