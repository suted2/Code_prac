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



