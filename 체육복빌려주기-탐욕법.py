'''def solution(n, lost, reserve): #적은 수의 학생수일때는 스캔하면 비효율
    list = [1] * (n+2)
    for l in lost:
        list[l]-=1
    for r in reserve:
        list[r]+=1
        
    for i in range(1,n+1):
        if list[i-1] == 0 and list[i]==2:
            list[i-1:i+1]=[1,1]
        if list[i+1]==0 and list[i]==2:
            list[i:i+2]=[1,1]

    return len([k for k in list[1:-1] if k>0])
'''

def solution(n,lost,reserve): #여벌은 적지만 n은 클때 여벌의 체육복을 갖고온 학생들만 고려
    s = set(lost) & set(reserve) #또이또이 맨
    l = set(lost) - s #없어 맨
    r = set(reserve) - s #두개 있어맨
    
    for x in sorted(r): #체육복을 빌려줄 수 있는 번호
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    return n - len(l)#빌려야 하는데 빌리지 못한 사람의 수 