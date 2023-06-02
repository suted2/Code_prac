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




# 다음 큰 숫자 

def solution(n):
    answer = 0
    ones_ = change(n).count('1') # 현재 숫자의 1의 개수를 구한다.  
    
    # 현재 숫자보다 큰 숫자이니까 앞으로 가면서 check 한다 . 
    
    while True:
        tmp = 0
        n += 1
        
        if change(n).count('1') == ones_:
            answer = n
            break
    
    
    return answer


def change(num):
    answer = []
    while True:
        answer.append(str(num % 2))
        num //= 2
    
        if num < 1:
            break
            
    return ''.join(answer[::-1])
        
        
###############################################



#영어 끝말잇기 

def solution(n, words):
    answer = []
    temp = {} # 중복 단어인지 체크하기!
    
    temp[words[0]] = 1 # 처음꺼 먼저 넣고 시작하자. 
    idx = 1 # 실패가 발생한 지점 체크하기
    
    while True: 
        
        if words[idx-1][-1] != words[idx][0]:
            idx += 1  # 번쨰를 구하기 위해 미리 더함 
            break
        else:
            if words[idx] in temp:
                idx += 1 # 번쨰를 구하기 위해 미리 더함 
                break
            else:
                temp[words[idx]] = 1
        

        if idx == len(words)-1:
            idx = 0 
            break
        idx += 1

    if idx == 0:
        return [0,0]
    
    else:
        person = 0 
        th = 0 
        if idx % n == 0:
            person = n
            th = idx // n
        else:
            person = idx % n 
            th = idx // n + 1 
        
        return [person, th]
############################################


# 카펫 

def solution(brown, yellow):
    answer = []
    #가로가 무조건 세로 이상이다. 
    
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i ==0:
            answer.append([i, yellow // i])
    
    tmp = []
    
    for j in answer:
        if (j[0]+2) * (j[1]+2) == (brown + yellow):
            return [j[1]+2, j[0]+2]
            
    
 ################################################

# 점프와 순간이동


def solution(n):
    
    # 순수 k칸 이동은 k칸의 cost가 발생한다. 
    # 순간이동은 현재 이동거리 * 2까지 갈수있지만 cost가 없다. 
    
    # 순간이동을 적극적으로 사용해야한다. 
    
    # 0 -> 1 은 무조건 움직여야함. 
    ans = 0 
    
    # n에서부터 나누면서 홀수가 나오는 개수가 곧 1칸씩 움직일 개수임. 
    while True: 

        if n % 2 == 0:
            n //= 2 
        elif n % 2 == 1: 
            ans +=1 
            n = (n-1) // 2 
        if n == 1: 
            break 
        if n == 0:
            return ans
            break
        
    # 마지막 0-> 1 가는 것까지 
    return ans+1

##################################################




