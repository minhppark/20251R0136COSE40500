from collections import deque

def dfs(graph, start, visited=None, depth=0):
    if visited is None:
        visited = set()
    visited.add(start)
    print("  " * depth + f"Visited {start}")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, depth + 1)
    return visited

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print(f"Starting BFS from {start}")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(f"Visited {node}")
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    return visited

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    print("Depth-First Search:")
    dfs(graph, 'A')
    print("\nBreadth-First Search:")
    bfs(graph, 'A')