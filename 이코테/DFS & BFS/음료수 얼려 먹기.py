import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(str,input())))

visited = [[False] * m for _ in range(n)]
cnt = 0

def dfs(a,b):
    visited[a][b] = True
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for ii in range(4):
        ax = a + dx[ii]
        ay = b + dy[ii]
        if 0 <= ax < n and 0 <= ay < m:
            if graph[ax][ay] == '0' and not visited[ax][ay]:
                dfs(ax,ay)


for nn in range(n):
    for mm in range(m):
        if not visited[nn][mm] and graph[nn][mm] == '0':
            dfs(nn,mm)
            cnt += 1

print(cnt)