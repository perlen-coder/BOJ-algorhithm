# format 함수 : 문자열을 보기 좋게 출력하기 위해 사용
# {}안에 출력할 형식을 지정하고, format()안에 값을 넣음
# 정수형 : {인자:0Nd}  -> N : 표현할 자릿수
#           ex. '{0:03d}'.format(1) => 001
# 실수형 : {인자:0.Nf} -> N : 소수점 아래 표시할 자릿수
#           ex. '{0:0.3f}'.format(1) => 1.000



n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    cnt = 0
    for j in scores[1:]:
        avg = sum(scores[1:]) / scores[0]
        # 평균보다 크면 카운트해줌
        if j > avg:
            cnt += 1
    rate = cnt / scores[0] * 100
    
    print('{0:0.3f}%'.format(rate))
