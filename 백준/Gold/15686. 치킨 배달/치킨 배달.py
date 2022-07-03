# 치킨거리 : abs(r1-r2) + abs(c1-c2)
# 리스트를 이용해서 집과 치킨집의 좌표를 저장
# itertools의 combinations를 이용
# -> 치킨집 리스트 chicken에서 m개 선택한 후, 치킨거리 구하면 됨.

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
res = 999999
home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

# 치킨집 m개 선택
for chic in combinations(chicken, m):
    tmp = 0  # 도시의 치킨거리
    for h in home: 
        chic_len = 999   # 각 집마다의 치킨 거리
        for j in range(m):
            chic_len = min(chic_len, abs(h[0] - chic[j][0]) + abs(h[1] - chic[j][1]))
        tmp += chic_len
    res = min(res, tmp)

print(res)