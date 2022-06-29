# 섬 : 한 개의 정사각형 or 가로ㆍ세로ㆍ대각선으로 연결되어 있는 사각형
#      -> 인접한 좌표들을 방문처리하여 하나의 섬으로 묶음
# 첫 번째 줄에, w(가로), h(세로) 입력 (0 < w,h <= 50)
# 두 번째 줄 부터, h개 줄에 지도가 주어짐. (땅 : 1, 바다 : 0)
# 입력의 마지막 줄에는 , 0 0 이 주어짐.


from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    
    # 상,하,좌,우 + 대각선 까지 고려해야하므로 -> 총 8방향으로 탐색
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    
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
    # 둘 다 0이면 종료
    #if not w and not h:
    if w == 0 and h == 0:
        break
    # 지도
    graph = [list(map(int, input().split())) for _ in range(h)]
    # 방문 체크
    visited = [[False]*w for _ in range(h)]
    count = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1    # bfs돌 때 마다 count +1
            else:
                continue
                
    print(count)