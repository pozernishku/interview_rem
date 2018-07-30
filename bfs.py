from collections import deque

def bfs(graph, root):
    '''Optimized BFS'''
    visited, explored, queue = set([root]), [], deque([root])
    levels = {}         # this dict keeps track of levels
    levels[root] = 0    # depth of root node is 0
    while queue:
        vertex = queue.popleft()
        explored.append(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

                levels[neighbour] = levels[vertex] + 1
    print(levels)
    return explored

graph = {0: [1, 2], 1: [2], 2: []}
# graph = {1: [2, 3], 2: [4, 6], 3: [7, 4], 4: [5], 5: [], 6: [], 7: [8], 8: []}
print(bfs(graph, 0))