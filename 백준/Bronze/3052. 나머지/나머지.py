# 서로 다른 값이 몇 개 있는지 출력
# -> 중복을 삭제하여 저장하는 집합 set() 사용! 

n = set()

for i in range(10):
    n.add(int(input()) % 42)
    
print(len(n))