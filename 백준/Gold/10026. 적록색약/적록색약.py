import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())

graph = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):

    visited.append((x, y))
    
    #방문하면 다시 방문하지 않도록 먼저 방문처리
    visited[x][y] = True
    
    # 상/하/좌/우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n) and visited[nx][ny] == False:
                if graph[nx][ny] == graph[x][y]:
                    dfs(nx,ny)

# 일반인의 경우
visited = [[False for _ in range(n)] for _ in range(n)]
cnt_1 = 0

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣음
        # if (i, j) not in visited:
        if not visited[i][j]:
            dfs(i, j)
            cnt_1 += 1


# 적록색약인이 보는 그림으로 변경 (G -> R로 변경)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 적록색약인의 경우
visited = [[False for _ in range(n)] for _ in range(n)]
cnt_2 = 0
for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣음
        # if (i, j) not in visited:
        if not visited[i][j]:
            dfs(i, j)
            cnt_2 += 1

print(cnt_1, cnt_2)