def dfs(graph, vertex, path=[]):
	path += [vertex]

	for neighbor in graph[vertex]:
		if neighbor not in path:
			path = dfs(graph, neighbor, path)

	return path

# a sample graph example
G = {1: [2, 3], 2: [4, 5],
	 3: [5], 4: [6], 5: [6],
	 6: [7], 7: []}

print(dfs(G, 1))