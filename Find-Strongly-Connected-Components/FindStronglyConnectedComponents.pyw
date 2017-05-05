from Tkinter import *
from math import *
fname = "dataset/AdjacentMatrix.txt"
adjacentMatrix = []

# Read from data file
try:
    fin = open(fname, "r")
    for line in fin.readlines():
        line = line.split()
        tmp = []
        for i in line:
            tmp.append(int(i))
        adjacentMatrix.append(tmp)
    fin.close()
    print "Read data from %s successfully!" % fname
except:
    print "Failed to read data!"
    exit

# Preprocessing, time complexity is O(|V|^2)
scale = len(adjacentMatrix) # number of vertices
forward = [] # adjacency list of the original graph
backward = [] # adjacency list of the reversed graph
for i in range(scale):
    forward.append([])
    backward.append([])
for i in range(scale):
    for j in range(scale):
        if adjacentMatrix[i][j]:
            forward[i].append(j)
            backward[j].append(i)

# DFS the reversed graph, time complexity is O(|V|+|E|)
def DFS(p):
    global clk
    visited[p] = 1
    for i in backward[p]:
        if visited[i] == 0:
            DFS(i)
    post[p] = clk
    postidx[clk] = p
    clk += 1
clk = 0
post = [0] * scale
postidx = [0] * scale
visited = [0] * scale
for i in range(scale):
    if visited[i] == 0:
        DFS(i)

# Finding strongly connected components, time complexity is O(|V|+|E|)
def findStronglyConnectedComponent(p):
    global tmp
    postidx[post[p]] = -1
    tmp.append(p)
    for i in forward[p]:
        if postidx[post[i]] != -1:
            findStronglyConnectedComponent(i)
pnt = scale - 1
res = []
while pnt >= 0:
    tmp = []
    findStronglyConnectedComponent(postidx[pnt])
    res.append(tmp)
    while pnt >= 0 and postidx[pnt] == -1:
        pnt -= 1

# Display the graph
def drawGrid():
    for i in range(1, grid):
        canvas.create_line(i * gridSize, 0, i * gridSize, windowSize, fill = 'grey')
    for i in range(1, grid):
        canvas.create_line(0, i * gridSize, windowSize, i * gridSize, fill = 'grey')    
def drawClique(x, y, direction, clique):
    size = len(clique)
    gap = pi * 2 / size
    x = (x + 0.5) * gridSize
    y = (y + 0.5) * gridSize
    for i in range(size):
        DIRECTION = direction + i * gap
        posX[clique[i]] = x + R * cos(DIRECTION)
        posY[clique[i]] = y - R * sin(DIRECTION)
        canvas.create_oval(posX[clique[i]] - r, posY[clique[i]] - r, posX[clique[i]] + r, posY[clique[i]] + r, fill = 'black')
        canvas.create_text(posX[clique[i]], posY[clique[i]], text=chr(65 + clique[i]), fill='white', font=('Arial',20,'normal'))
def drawArrow(i, j):
    x1, y1 = posX[i], posY[i]
    x2, y2 = posX[j], posY[j]
    dis = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    dx, dy = (x2 - x1) / dis * r, (y2 - y1) / dis * r
    x1 += dx
    y1 += dy
    x2 -= dx
    y2 -= dy
    canvas.create_line(x1, y1, x2, y2, arrow = "last")
windowSize = 600
res.reverse()
cliques = len(res)

# Print the result in command line
print "The result is:"
for i in range(cliques):
    print "%d:"%(i+1),
    for j in res[i]:
        print chr(65+j),
    print

# Draw the graph
grid = int(sqrt(cliques))
gridSize = windowSize / grid
R = gridSize * 0.32
r = gridSize * 0.08
posX = [0] * scale
posY = [0] * scale
window = Tk()
window.title("Find Strongly Connected Components")
window.geometry(str(windowSize)+'x'+str(windowSize))
canvas = Canvas(window, height = windowSize, width = windowSize, bg = 'white')
canvas.pack()
drawGrid()
for i in range(cliques):
    y = i / grid
    X = i % grid
    if y % 2 == 1:
        direction = 0
        x = grid - 1 - X
    else:
        direction = pi
        x = X
    if i > 0 and X == 0:
        direction = pi / 2
    drawClique(x, y, direction, res[i])
for i in range(scale):
    for j in forward[i]:
        drawArrow(i, j)
window.mainloop()
