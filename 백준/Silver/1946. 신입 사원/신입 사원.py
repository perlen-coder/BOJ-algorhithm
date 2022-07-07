# 일단, 어떤 성적이든 1등한 사람은 무조건 뽑힘.
# 만약, 서류 성적 2등이 서류 성적 1등보다 면접 등수가 높으면 뽑힘
# 서류 성적 3등이 서류 성적 1,2등보다 면접 등수가 높으면 뽑힘

import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    ranks = [list(map(int, input().split())) for _ in range(n)]
    
    sorted_ranks = sorted(ranks, key = lambda x:x[0])
    cnt = 1
    person = sorted_ranks[0][1]
    for j in range(1,n):
        if sorted_ranks[j][1] < person:
            person = sorted_ranks[j][1]
            cnt += 1
            
    print(cnt)