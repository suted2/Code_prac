#########################

#Jaden Case

def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):

        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer
  
  
 ###################################


#최대값과 최소값


def solution(s):
    answer = ''
    tmp = []
    for i in s.split():
        tmp.append(int(i))
        
    answer += str(min(tmp))
    answer += ' '
    answer += str(max(tmp))
    
    
    return answer
  
  
#####################################



# 올바른 괄호 



def solution(s):
    answer = True
    
    s = list(s)
    temp = [] # ')'저장하다가 '(' 나오면 하나씩 지울 스택 
    temp2 = []
    if s[0] == ')' or s[-1] == '(':
        return False
    
    else:
        for _ in range(len(s)):
            if s[-1] == ')':
                temp.append(')')
                s.pop()
            else:
                if temp:
                    s.pop()
                    temp.pop()
                else:
                    return False
    return answer

#################################################



# 이진변환 반복하기 

def solution(s):
    cnt = 0 # 이진 변환의 실행 횟수를 체크할 곳 
    cnt_zero = 0 # 사라진 0의 개수 체크할 곳     
    while True:


        cnt_zero += s.count('0')
        s = s.replace('0', '') #이진변화(1) 0을 제거 

        s = ''.join(change_num(len(s))) #남은 문자열의 길이를 변환 ! 
        cnt += 1 # 실행횟수 + 1
        if s == '1': 
            break
    
    
    return [cnt, cnt_zero]

def change_num(num): # 2진법으로 바꾸는 함수 
    temp = []
    while True: 
        temp.append(str(num % 2))
        num //= 2
        if num < 1: 
            break
    return temp[::-1]


##################################


#숫자의 표현 

def solution(n):
    answer = 0
    # 완전 탐색의 방법 
    for i in range(1, n+1): # 기준이 되는 숫자 for 문
        sum = 0
        for j in range(i, n+1): #기준이 되는 숫자에서 연속되게 더한다. 
            sum += j
            if sum == n: # 정확하게 n이 나오면 answer +=1 
                answer+=1 
                break
            elif sum > n: # n을 한번 초과하면 답이 나올 가능성이 없어서 바로 break 
                break
    return answer
    
    
    
    return answer


####################################
