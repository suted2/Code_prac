############제목 : 내적############################ 

 def solution(a, b): 
        
        answer = 0
        for i,j in zip(a,b): #같은 길이의 배열이라고 지정을 해두었기에 zip으로 묶어 사용했다. 
        answer += i*j

        return answer
      
     
############################
#문자열 다루기 기본




def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s:
        if i.isalpha():
            return False
            break

    return answer
  
###########################  


#푸드 파이트 대회 

def solution(food):
    
    tmp = {}
    for idx, i in enumerate(food):
        tmp[idx] = i // 2 # 짝수개의 음식만 쓸수 있고 좌우 중복이니까 절반만 가지고 와서 배치하자 
        
    tmp2 = [] 
    for x, y in tmp.items(): 
        if x == 0:
            continue
        if y != 0:
            for k in range(y):
                tmp2.append(str(x)) ## list에 하나씩 해당 인덱스의 개수만큼 ( 음식의 개수 ) append해서 만들어준다. 
                

    answer = tmp2 + ['0'] + tmp2[::-1] # 절반의 배열과 가운데의 0 , 나머지는 뒤집힌 기존 배열을 더한후 
    return ''.join(answer) # 리스트를 하나의 문자열로 합쳐 준다.
  
  
  
  ###########################
  
  #같은 숫자는 싫어 

def solution(arr):
    answer = []
    
    #돌면서 앞에 인덱스랑 다르면 추가하기 
    answer.append(arr[0])
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    
    return answer
  
  
  
  ###########################


  
  
#크기가 작은 부분 문자열

def solution(t, p):
    answer = 0
    num = len(p)
    for i in range(0, len(t)-num+1):
        if int(p) >= int(t[i:i+num]):
            answer += 1 
    return answer

##############################


#로또의 최고순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    cnt = 0  #  이미 같은 숫자 세기 
    cnt_zero = 0  # 여러 숫자로 변할 수 있는 0의 개수 구하기 
    for i in lottos: 
        if i in win_nums:
            cnt += 1
        elif i == 0:
            cnt_zero +=1 
    
    # 최저 등수 == 현재 cnt의 개수 
    # 최대 등수 == 현재 cnt의 개수 + 0의 개수 
    
    #순위 == 7 - 맞춘개수, 단 0개를 맞춰도 낙첨이기에 예외처리가 필요하다. 
    
    if cnt + cnt_zero <= 1:
        max_num = 6
    else:
        max_num = 7 - (cnt + cnt_zero)
    
    if cnt <= 1:
        min_num = 6
    else:
        min_num = 7 - cnt
            
    return [max_num, min_num]
  
 
###########################################################


#문자열 내림차순으로 배치하기 



def solution(s):
    answer = ''
    lower = [] 
    upper = [] 
    
    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    
    lower.sort(reverse = True)
    upper.sort(reverse = True) 
    
    tmp = lower + upper 
    
    return ''.join(tmp)
  
  
###############################################



#문제 설명


def solution(a, b):
    days = [31, 29, 31, 30 , 31 , 30 ,31, 31 ,30 , 31 , 30 , 31]  # 1~12월이 가진 일수 
    week = ['THU', 'FRI', 'SAT', 'SUN', "MON", 'TUE', 'WED'] # 1월1일이 금요일이기에 나누면 나머지가 요일이 될 수 있게 list를 만들어 둔다. 
    tmp = 0
    for i in range(a-1): # a가 해당하는 달 이전 달까지는 전부 더함 
        tmp += days[i]
    
    tmp+= b #요일 더해준다. 
    
    
    
    return week[tmp % 7]
   
 ###############################################
 
 
 
 #약수의 개수와 덧셈 
 
 
 
 def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        tmp = check_num(i)
        if tmp % 2 ==0: #짝수면 더하고 
            answer += i
            
        else:
            answer -= i #홀수면 빼기 
    return answer



def check_num(num): # 약수의 개수를 구하기 위한 식 
    cnt = 0
    for i in range(1,num+1):
        if num % i ==0:
            cnt +=1
            
    return cnt
 
 
 
 ################################################
 
 
 
 #폰켓몬 
 
 
 def solution(nums):
    answer = 0
    N = len(nums)
    nums = set(nums)
    answer = len(nums)
    
    if len(nums) > N/2:
        answer = N/2
    return answer
   
####################################



# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        tmp = []
        for x,y in zip(i,j):
            
            tmp.append(x+y)
        answer.append(tmp)
            
    return answer
   
################################




# 모의고사

def solution(answers):
    answer = []
    #1번 학생, 2번학생, 3번학생 룰 
    rule1 = [1,2,3,4,5]
    rule2 = [2,1,2,3,2,4,2,5]
    rule3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = check(answers, rule1)
    cnt2 = check(answers, rule2)
    cnt3 = check(answers, rule3)
    tmp = [cnt1,cnt2,cnt3]
    max_value = max(tmp)

    for idx, i in enumerate(tmp):
        if  i == max_value:     
            answer.append(idx+1)
    return sorted(answer)

def check(answers, rule):
    cnt = 0 
    if len(rule) < len(answers):
        tmp = rule * (len(answers) // len(rule) + 1)
        tmp = tmp[:len(answers)]
    elif len(rule) == len(answers):
        tmp = rule
    else:
        tmp = rule[:len(answers)]
        
    for i in range(len(answers)):
        if answers[i] == tmp[i]:
            cnt += 1 
    
    return cnt 
    
#############################################




# 3진법 뒤집기

def solution(n):
    answer = 0
    tmp = []
    while True:
        tmp.append(str(n % 3))
        n //= 3
        
        if n < 1:
            break

    num = 1 
    tmp = tmp[::-1]
    for i in tmp:
        answer += int(i) * num
        num *= 3
        
    return answer
   
   
########################################



# 이상한 문자열 만들기


def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]
 
##########################################



# 최소 직사각형

def solution(sizes):
    answer = 0
    tmp = []
    tmp1 = []
    
    for x,y in sizes:
        tmp.append(min(x,y))
        tmp1.append(max(x,y))
        
    
    answer = max(tmp) * max(tmp1)
    return answer
   
   
#############################################




# 콜라 문제 


def solution(a, b, n):
    answer = 0
    tmp = 0  # 나머지를 저장해둘 숫자 .
    
    while True:
        #b * (n // a)  # 현재 가진 병으로 받을 수 있는 숫자. 
        #n % a # 남은 병 수 .
        answer += b * (n // a) # 받은 숫자는 저장하고 
        tmp = n % a 
        #현재 병의 숫자로 n을 초기화 해주고 받은 숫 자 + 나머지 
        n = b * (n // a) + tmp
        if n < a:
            break
    
    return answer
   
   
##############################################
