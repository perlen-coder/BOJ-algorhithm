"""
1. 아이디어
- 2중 for, 값 1 && 방문X => DFS 수행
- DFS를 통해 찾은 값을 저장 후, 정렬 해서 출력

2. 시간복잡도
- DFS : O(V+E)
- V, E : N^2, 4N^2
- V+E : 5N^2 ~= N^2 ~= 625 > 2억 ∴ 가능

3. 자료구조
- 그래프 정보 저장 : int[][] -> 2차원 배열
- 방문 여부 체크 : bool[][] -> 2차원 배열
- 결과값 저장 : int[]
"""

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
res = []    # 결과값 저장할 리스트
each = 0    # dfs 새로 수행할 때 마다 갱신하기위한 변수

# 상,하,좌,우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if (0 <= ny < n) and (0 <= nx < n):
            if graph[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(n):
    for i in range(n):
        if graph[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True    # 방문 체크 표시
            each = 0    # 매번 값을 구해야할 때 마다, 0으로 초기화
            dfs(j,i)    # dfs로 크기 구하기 (그래프 탐색)
            res.append(each)    # 결과값을 리스트에 넣음

res.sort()    # 정렬

print(len(res))
for i in res:
    print(i)