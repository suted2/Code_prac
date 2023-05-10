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


# 크레인 인형뽑기 

def solution(board, moves):
    bucket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer)*2


########################
