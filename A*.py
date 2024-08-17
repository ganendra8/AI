import heapq

graph = {
    '5': [('3', 2), ('7', 4)],
    '3': [('2', 1), ('4', 3)],
    '7': [('8', 1)],
    '2': [],
    '4': [('8', 2)],
    '8': []
}

# Heuristic function h(n)
heuristic = {
    '5': 6,
    '3': 4,
    '7': 2,
    '2': 7,
    '4': 2,
    '8': 0
}

def astar(graph, start, goal):
    # Priority queue to store (f_cost, g_cost, node) tuples
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start))
    
    visited = set()

    while pq:
        # Pop the node with the smallest f_cost
        f_cost, g_cost, node = heapq.heappop(pq)

        # If the node is the goal, return the path
        if node == goal:
            print(f"Reached goal {node} with cost {g_cost}")
            return

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)
        print(f"Visited {node} with cost {g_cost}")

        # Explore neighbors
        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                new_g_cost = g_cost + edge_cost
                new_f_cost = new_g_cost + heuristic[neighbour]
                heapq.heappush(pq, (new_f_cost, new_g_cost, neighbour))

# Driver Code
print("Following is the A* Search")
astar(graph, '5', '8')
