import sys
from collections import defaultdict
import topological_sort

N = 0 # ok
T = 0 # ok
M = 0 # ok
K = 0 # ok
EST = defaultdict(int) # ok
EFT = defaultdict(int) # ok
LST = defaultdict(int) # ok
LFT = defaultdict(int) # ok
d = [None] # ok
R = [None] # ok

g = topological_sort.Graph()

flag = 0 # 分成 PRECEDENCE RELATIONS、REQUESTS/DURATIONS、RESOURCEAVAILABILITIES 三部分
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        if line == 'PRECEDENCE RELATIONS:\n': flag = 1
        if line == 'REQUESTS/DURATIONS:\n': flag = 2
        if line == 'RESOURCEAVAILABILITIES:\n': flag = 3
        lines = line.split()
        if flag == 1:
            if lines[0].isdigit():
                del lines[1]
                lines = list(map(lambda x: int(x), lines))
                assert len(lines) == lines[1] + 2
                del lines[1]
                for v in lines[1:]:
                    g.addEdge(lines[0], v)
        if flag == 2:
            if lines[0].isdigit():
                del lines[1]
                lines = list(map(lambda x: int(x), lines))
                assert lines[0] == len(d) == len(R)
                d.append(lines[1]) # write d
                del lines[1]
                if K == 0: K = len(lines[1:]) # write K
                else: assert K == len(lines[1:])
                R.append(lines[1:]) # write R
        if flag == 3:
            if lines[0].isdigit():
                lines = list(map(lambda x: int(x), lines))
                M = max(lines) # write M

assert len(d) == len(R)
N = len(d) - 1 # write N
assert len(g.parents) == N - 1

topological_order = g.topologicalSort()
# print(topological_order)

for v in topological_order:
    EST[v] = max(map(lambda x: EFT[x], g.parents[v]), default=0) # write EST
    EFT[v] = EST[v] + d[v] # write EFT
    # print(v, EST[v], EFT[v])

for v in reversed(topological_order):
    LFT[v] = min(map(lambda x: LST[x], g.children[v]), default=EFT[v]) # write LFT
    LST[v] = LFT[v] - d[v] # write LST
    # print(v, LST[v], LFT[v])

assert EFT[topological_order[-1]] == LFT[topological_order[-1]]
T = EFT[topological_order[-1]] # write T

###############################################################

with open('data.run', 'w') as f:
    print('data;', file=f)
    print(file=f)
    print(f'param N := {N};', file=f)
    print(f'param T := {T};', file=f)
    print(f'param M := {M};', file=f)
    print(f'param K := {K};', file=f)
    print('param: EST :=', file=f)
    for i in range(1, 1+N):
        print(i, EST[i], file=f)
    print(';', file=f)
    print('param: EFT :=', file=f)
    for i in range(1, 1+N):
        print(i, EFT[i], file=f)
    print(';', file=f)
    print('param: LST :=', file=f)
    for i in range(1, 1+N):
        print(i, LST[i], file=f)
    print(';', file=f)
    print('param: LFT :=', file=f)
    for i in range(1, 1+N):
        print(i, LFT[i], file=f)
    print(';', file=f)
    print('param: d :=', file=f)
    for i in range(1, 1+N):
        print(i, d[i], file=f)
    print(';', file=f)
    print('param: R :=', file=f)
    for i in range(1, 1+N):
        for j in range(K):
            print(i, j+1, R[i][j], file=f)
    print(';', file=f)