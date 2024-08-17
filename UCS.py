import heapq

graph = {
    '5': [('3', 2), ('7', 4)],
    '3': [('2', 1), ('4', 3)],
    '7': [('8', 1)],
    '2': [],
    '4': [('8', 2)],
    '8': []
}

def ucs(graph, start):
    # Priority queue to store (cost, node) tuples
    pq = []
    heapq.heappush(pq, (0, start))
    
    visited = set()

    while pq:
        # Pop the node with the smallest cost
        cost, node = heapq.heappop(pq)

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)
        print(f"Visited {node} with cost {cost}")

        # Explore neighbors
        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbour))

# Driver Code
print("Following is the Uniform Cost Search")
ucs(graph, '5')
