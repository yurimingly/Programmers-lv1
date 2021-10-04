'''def solution(n, lost, reserve):
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

def solution(n,lost,reserve):
    s = set(lost) & set(reserve) #또이또이 맨
    l = set(lost) - s #없어 맨
    r = set(reserve) - s #있어맨
    
    
    
    
    return answer