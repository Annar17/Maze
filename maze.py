M = 6 # Rows
N = 3 # Columns

def isSafe(maze, visited, x, y):
    if maze[x][y] == 0 or visited[x][y] == True:
        return False # Unsafe
    return True # Safe

def isValid(x, y):
    if x < M and y < N and x >= 0 and y >= 0 and maze[x][y] == 1:
        return True # Valid
    return False # Invalid

def solve(maze, visited, i, j, dest_x, dest_y, curr_dist, min_dist, shortestPath, currentPath):
    if i==dest_x and j==dest_y: 
        if curr_dist<min_dist[0]:
            min_dist[0] = curr_dist
            shortestPath.clear()
            shortestPath.extend(currentPath)
            shortestPath.append((dest_y,dest_x))
            return

    # set (i, j) cell as visited
    visited[i][j] = True
    currentPath.append((j,i))

    # BOTTOM
    if isValid(i + 1, j) and isSafe(maze, visited, i + 1, j):
        solve(maze, visited, i + 1, j, dest_x, dest_y, curr_dist + 1, min_dist, shortestPath, currentPath)

    # RIGHT
    if isValid(i, j + 1) and isSafe(maze, visited, i, j + 1):
        solve(maze, visited, i, j + 1, dest_x, dest_y, curr_dist + 1, min_dist, shortestPath, currentPath)
        
    # TOP
    if isValid(i - 1, j) and isSafe(maze, visited, i - 1, j):
        solve(maze, visited, i - 1, j, dest_x, dest_y, curr_dist + 1, min_dist, shortestPath, currentPath)
        
    # LEFT
    if isValid(i, j - 1) and isSafe(maze, visited, i, j - 1):
        solve(maze, visited, i, j - 1, dest_x, dest_y, curr_dist + 1, min_dist, shortestPath, currentPath)
       
    visited[i][j] = False
    currentPath.pop()

if __name__ == "__main__": 
    min_dist = [1000]
    shortestPath = [] 
    currentPath = []
    maze = [ [1, 0, 0],
             [1, 1, 1],  
             [1, 0, 1], 
             [1, 0, 1], 
             [1, 1, 1],
             [1, 0, 0] ]

    visited = []
    for i in range(M):
        lst = list()
        for j in range(N):
            lst.append(False)
        visited.append(lst)
    solve(maze, visited, 0, 0, M-1, 0, 0, min_dist, shortestPath, currentPath)
    
    slt = [ [ 0 for i in range(N) ] for j in range(M) ] 

    print("Distance: ", min_dist[0])
    print("Path: [", end=" ")
    for path in shortestPath:
        print('('+str(path[0])+','+str(path[1])+')',end=" ")
        slt[path[1]][path[0]] = 1
    print("]")
    for i in range(len(slt)):
        for j in range(len(slt[i])):
            print(slt[i][j], end=' ')
        print()
 