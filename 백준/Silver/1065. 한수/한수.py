n = int(input())
hansoo = 0

for n in range(1, n+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansoo += 1 
    
    else :     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리 
        if (nums[0] - nums[1]) == (nums[1] - nums[2]) : #등차수열 확인
            hansoo+=1

print(hansoo)