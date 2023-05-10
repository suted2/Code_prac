##########################3


# 소수 찾기 

def solution(n):
    answer = 0
    
    for i in range(3,n+1):
        if check_num(i):
            answer +=1
    
    return answer+1

def check_num(n):
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            flag = False
            return flag
            break
    return flag
  
########################
