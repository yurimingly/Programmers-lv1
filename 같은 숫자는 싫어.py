'''
https://programmers.co.kr/learn/courses/30/lessons/12906

같은 숫자는 싫어

darklight

sublimevimemacs

문제 설명

배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.

arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

제한사항

배열 arr의 크기 : 1,000,000 이하의 자연수

배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

입출력 예


0열 선택0열 다음에 열 추가
1열 선택1열 다음에 열 추가
0행 선택0행 다음에 행 추가
1행 선택1행 다음에 행 추가
2행 선택2행 다음에 행 추가
셀 전체 선택
열 너비 조절
행 높이 조절
arr

answer

[1,1,3,3,0,1,1]

[1,3,0,1]

[4,4,4,3,3]

[4,3]

셀 병합
행 분할
열 분할
너비 맞춤
삭제
입출력 예 설명

입출력 예 #1,2

문제의 예시와 같습니다.

'''

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i ==0: answer.append(arr[i])
        if answer[-1] == arr[i]: continue 
        else: answer.append(arr[i])
    return answer
