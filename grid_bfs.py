rows = 4
cols = 4

grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,0,1],
]

visited = set()
directions = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and (i,j) not in visited:

            
