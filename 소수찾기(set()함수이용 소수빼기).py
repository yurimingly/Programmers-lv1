'''
https://programmers.co.kr/learn/courses/30/lessons/12921

소수 찾기

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

def solution(n):
    num = set(range(2,n+1)) #어차피 1은 안되니까 2부터 시작, n=10이면 +1로 해서 10도 포함되게

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i)) #n=2이면 4부터 11까지 2씩 증가 set에는 4,8,10,6이 담겨있음
    return len(num)

n=10
solution(n)