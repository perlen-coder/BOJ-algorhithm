n = int(input())
score = list(map(int, input().split()))
M = max(score)

n_score = [ (i/M)*100 for i in score ]

print(sum(n_score)/n)