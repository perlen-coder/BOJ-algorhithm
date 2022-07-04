n = int(input())

for i in range(n):
    ox = input()
    
    score = 0
    sum_score = 0
    for j in ox:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
        
    print(sum_score)