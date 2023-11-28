import sys

def process_input():
    graph = {}
    num_vertices, num_edges = map(int, sys.stdin.readline().split())
    for i in range(1, num_vertices+1):
        graph[i] = {}
    for _ in range(num_edges):
        start, end, weight = map(int, sys.stdin.readline().split())
        graph[start][end] = weight
    start, end = map(int, sys.stdin.readline().split())
    return graph, start, end

def dijkstra(graph, start, end):
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0

    visited = set()

    while len(visited) < len(graph):
        min_distance = sys.maxsize
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        visited.add(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            new_distance = distances[min_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances[end] if distances[end] != sys.maxsize else -1


print(dijkstra(*process_input()))
