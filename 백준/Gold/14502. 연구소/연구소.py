# 0 : 빈칸, 1 : 벽, 2 : 바이러스
# 안전 영역 : 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳 (0의 개수)
# 안전 영역 크기의 최댓값을 구하는 프로그램 작성하라

# 벽은 반드시 3개를 세워야함
# 벽을 3개 세우고 바이러스를 퍼트림
# 바이러스가 상하좌우로 이동하므로 -> bfs or dfs

from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

graph = []          # 처음 입력받은 정보를 저장할 리스트
tmp = [[0]* m for _ in range(n)]    # 벽을 세운 뒤 저장할 리스트
res = 0

# 그래프 정보 입력받기
for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip().split())))
    
# 상,하,좌,우 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 바이러스 퍼트리는 함수
def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상,하,좌,우로 퍼질 수 있으면 
        if (0 <= nx < n) and (0 <= ny < m):
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2     # 그 위치에 바이러스 배치
                virus(nx,ny)        # 재귀함수로, 반복수행
    return

# 현재 그래프에서 안전 영역 계산하는 함수
def safearea_count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt
    
# 벽을 세울 때 마다, 매번 안전 영역 계산
def dfs(cnt):
    global res
    
    # 벽이 3개인 경우
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                # 현 위치에 바이러스가 있다면, 바이러스 확산
                if tmp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최대값 계산
        res = max(res, safearea_count())
        return
    # 0(빈 칸)에 벽 세우기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                dfs(cnt)
                graph[i][j] = 0
                cnt -= 1
                
dfs(0)
print(res)