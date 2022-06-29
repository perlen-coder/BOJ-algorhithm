from collections import deque
import sys;


# 상,하,좌,우 + 대각선 까지 고려해야하므로 -> 총 8방향으로 탐색
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
 
    while q:
        x, y = q.popleft()
 
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    
while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
 
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    print(count)