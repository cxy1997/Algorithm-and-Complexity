from Tkinter import *
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
fname = 'dataset\\testcase.txt'
radius = 4
def adjustX(x):
    return (x - minX) / xRange * 800 + 112
def adjustY(y):
    return (maxY - y) / yRange * 600 + 84
def drawCircle(canvas, p):
    x = adjustX(p.x)
    y = adjustY(p.y)
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, width = 1)
def qsort(points, l, r):
    if l >= r:
        return
    i, j = l, r
    tmp = points[i]
    while i < j:
        while i < j and points[j].x > tmp.x:
            j -= 1
        points[i] = points[j]
        while i < j and points[i].x < tmp.x:
            i += 1
        points[j] = points[i]
    points[i] = tmp
    qsort(points, l, i - 1)
    qsort(points, i + 1, r)
#########################################################
try:
    dataset = open(fname, 'r')
    points = []
    n, c = dataset.readline().split('\t')
    n, c = int(n), float(c)
    for i in range(n):
        x, y = dataset.readline().split()
        x, y = float(x), float(y)
        points.append(point(x, y))
        if i == 0:
            minX, maxX, minY, maxY = x, x, y, y
        else:
            if minX > x:
                minX = x
            if maxX < x:
                maxX = x
            if minY > y:
                minY = y
            if maxY < y:
                maxY = y
    dataset.close()
    xRange = maxX - minX
    yRange = maxY - minY
except:
    print 'Fail to load dataset.\nPress <Enter> to exit.'
    raw_input()
qsort(points, 0, n - 1) #sort by coordinate x in increasing order
a, b, e = [], [], []
OPT = [0] * n
last = [-1] * n
for i in range(1, n + 1):
    a.append([0] * i)
    b.append([0] * i)
    e.append([0] * i)
for i in range(n):
    x, y = points[i].x, points[i].y
    xy, x2, y2 = x * y, x * x, y * y
    tn = 1
    for j in range(i + 1, n):
        x += points[j].x
        y += points[j].y
        xy += points[j].x * points[j].y
        x2 += points[j].x * points[j].x
        y2 += points[j].y * points[j].y
        tn += 1
        a[j][i] = (tn * xy - x * y) / (tn * x2 - x * x)
        b[j][i] = (y - a[j][i] * x) / tn
        e[j][i] = y2 + a[j][i] * a[j][i] * x2 + tn * b[j][i] * b[j][i] \
                  +2 * (a[j][i] * b[j][i] * x - a[j][i] * xy - b[j][i] * y)
for j in range(n):
    Min = e[j][0]
    for i in range(1, j + 1):
        tmp = e[j][i] + OPT[i - 1]
        if Min > tmp:
            last[j] = i - 1
            Min = tmp
    OPT[j] = Min + c
    print 'OPT[%d] = %0.4f'%(j + 1, OPT[j])
edges = []
end = n - 1
while end >= 0:
    edges.append([last[end] + 1, end])
    end = last[end]
edges.reverse()
root = Tk()
root.title('Segmented Least Square')
root.geometry('1024x768')
canvas = Canvas(root, height = 768, width = 1024, bg = 'white')
canvas.pack()
for i in range(n):
    drawCircle(canvas, points[i])
canvas.create_line(112, 84, 112, 684, arrow = FIRST)
canvas.create_line(112, 684, 912, 684, arrow = LAST)
canvas.create_text(102, 87, text = 'y')
canvas.create_text(907, 692, text = 'x')
canvas.create_text(102, 692, text = '0')
L = len(edges)
patition = [0] * (L + 1)
patition[0] = (3 * points[0].x - points[1].x) / 2
patition[L] = (3 * points[n - 1].x - points[n - 2].x) / 2
for i in range(1, L):
    tmp = (b[edges[i][1]][edges[i][0]] - b[edges[i-1][1]][edges[i-1][0]]) / (a[edges[i-1][1]][edges[i-1][0]] - a[edges[i][1]][edges[i][0]])
    if points[edges[i-1][1]].x < tmp < points[edges[i][0]].x:
        patition[i] = tmp
    else:
        patition[i] = (points[edges[i - 1][1]].x + points[edges[i][0]].x) / 2
for i in range(L):
    canvas.create_line(adjustX(patition[i]),
                       adjustY(a[edges[i][1]][edges[i][0]] * patition[i] + b[edges[i][1]][edges[i][0]]),
                       adjustX(patition[i+1]),
                       adjustY(a[edges[i][1]][edges[i][0]] * patition[i+1] + b[edges[i][1]][edges[i][0]]),
                       fill = 'blue', width = 2)
root.mainloop()
