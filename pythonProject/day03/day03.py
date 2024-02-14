graph= [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
]

graph2= [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]

graph2= [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]


graph3= [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]

name_arr = ['mb','sr','hi','zz','sm','hs']

def dfs(g, v, visited) :
    visited[v] = True
    print(name_arr[v], end =' ')
    for i in range(len(g)):
        if g[v][i] == True and not visited[i]:
            dfs(g, i, visited)

visited = [False] * len(graph3)
dfs(graph3, 0, visited)