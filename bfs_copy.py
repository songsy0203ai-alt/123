# bfs_copy.py

myGraph = graph = {'A':['B','C','D'], 
         'B':['A','E'], 
         'C':['A','F','G'], 
         'D':['A','H'], 
         'E':['B','I'], 
         'F':['C','J'],
         'G':['C'],
         'H':['D'], 
         'I':['E'], 
         'J':['F'],
         'K':['A','B']}

def my_bfs(graph, start_node):
    queue = list()
    visited = list()
    queue.append(start_node) # Enqueue

    while queue:
        node = queue.pop(0) # Dequeue

        if node not in visited:
            queue.extend(graph[node])
            visited.append(node)
    
    print(f"bfs - {visited}")
    return visited

my_bfs(myGraph, 'A')