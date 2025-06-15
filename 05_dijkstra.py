import heapq

def dijkstra(graph, start):
    print(f"Running Dijkstra's algorithm from {start}")
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        print(f"Visiting {current_node} with current distance {current_distance}")

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            print(f"Checking neighbor {neighbor} with edge weight {weight}")
            if distance < distances[neighbor]:
                print(f"Updating distance of {neighbor} to {distance}")
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    result = dijkstra(graph, 'A')
    for node in result:
        print(f"Shortest distance to {node}: {result[node]}")