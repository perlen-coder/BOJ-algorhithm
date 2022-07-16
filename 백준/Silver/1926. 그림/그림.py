'''
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS 수행
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 ∴ 가능!

3. 자료구조
- 그래프 전체 지도 : int[][] -> 2차원 배열
- 방문 여부 : bool[][] -> 2차원 배열
- Queue(BFS) 사용
'''

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 입력받은 지도 : 2차원 배열
graph = [list(map(int, input().split())) for _ in range(n)]
# 방문 여부 체크 : 2차원 배열
chk = [[False]*m for _ in range(n)]

# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y,x):
    
    res = 1    # 그림의 크기(size)
    q = deque()
    q.append((y,x))
    
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if (0 <= ny < n) and (0 <= nx < m):
                if graph[ny][nx] == 1 and chk[ny][nx] == False:
                    res += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return res


cnt = 0    # 전체 그림 개수
maxv = 0    # 최대값

for j in range(n):
    for i in range(m):
        if graph[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))
            
print(cnt)
print(maxv)