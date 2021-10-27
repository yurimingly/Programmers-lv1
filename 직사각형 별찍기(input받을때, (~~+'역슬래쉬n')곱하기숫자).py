'''
https://programmers.co.kr/learn/courses/30/lessons/12969

직사각형 별찍기

이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

제한 조건
n과 m은 각각 1000 이하인 자연수입니다.
예시
입력

5 3
출력

*****
*****
*****
'''

a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

'''내가 푼 방식 미련ver.
a, b = map(int, input().strip().split(' '))

for i in range(b):
    answer = ''
    for k in range(a):
        answer += '*'
    print(answer)

다들 미련하게 풀었다고 한다...비난하지마광광
'''