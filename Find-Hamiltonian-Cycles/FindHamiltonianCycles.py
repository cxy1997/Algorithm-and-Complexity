# Find Hamiltonian cycles in a specific graph
# Node 0: the starting node
# Node 1-16: x1
# Node 17-32: x2
# Node 33-48: x3
# Node 49: the terminal node
# Node 50-57: clause nodes

forward = [[1, 16], [2, 17, 32]]
for i in range(2, 16):
    forward.append([i-1, i+1])
forward.append([15, 17, 32])
forward.append([18, 33, 48])
for i in range(18, 32):
    forward.append([i-1, i+1])
forward.append([31, 33, 48])
forward.append([34, 49])
for i in range(34, 48):
    forward.append([i-1, i+1])
forward.append([47, 49])
for i in range(9):
    forward.append([])
for i in range(2):
    for j in range(2):
        for k in range(2):
            num = i * 4 + j * 2 + k
            clause = num + 50
            x1 = 1 + num * 2
            x2 = 17 + num * 2
            x3 = 33 + num * 2
            if i:
                forward[x1].append(clause)
                forward[clause].append(x1 + 1)
            else:
                forward[x1 + 1].append(clause)
                forward[clause].append(x1)
            if j:
                forward[x2].append(clause)
                forward[clause].append(x2 + 1)
            else:
                forward[x2 + 1].append(clause)
                forward[clause].append(x2)
            if k:
                forward[x3].append(clause)
                forward[clause].append(x3 + 1)
            else:
                forward[x3 + 1].append(clause)
                forward[clause].append(x3)
visited = [False] * 58
cnt = 0
idx = 0
record = [0] * 57 + [49]
find = False
def DFS(n):
    global cnt
    global idx
    global find
    if n == 49:     # Terminal point
        if idx == 57:
            print record
            cnt += 1
            find = True
        return
    visited[n] = True
    record[idx] = n
    idx += 1
    for i in forward[n]:
        if not visited[i]:
            DFS(i)
    visited[n] = False
    idx -= 1
DFS(0)
if find:
    print "There are %d Hamiltonian cycles in total."%cnt
else:
    print "Hamiltonian cycle Not find."
raw_input()
