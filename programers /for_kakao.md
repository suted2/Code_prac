## kakao 기출 문제 풀어보기 



### 1. 캐시 

```python
def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0: 
        return len(cities) * 5
    
    tmp = []
    for city in cities:
        city = city.lower() # 대소문자 구분이 없으므로 
        
        if not city in tmp:
            if len(tmp) == cacheSize:
                tmp.pop(0)
                tmp.append(city)
                answer += 5 
            else:
                tmp.append(city)
                answer += 5
        
        else:
            tmp.pop(tmp.index(city))
            tmp.append(city)
            answer += 1 
        
    return answer

```


🤔




1. LRU 의 경우는 가장 이전의 것을 제거하는 방식임. 
2. 캐시 hit == buffer에 이미 존재하는 것을 찾은 경우 -> 기존에 buffer에 있던 동일 캐시 삭제 
3. 캐시 miss == buffer에 없던 새로운 것을 넣는 경우 -> 기존에 buffer에 cashsize를 check하고 넣는다. 





### 2. 튜플


```python

import re 
def solution(s):
    answer = []
    
    s = s[2:-2] # 시작과 끝에는 {{,}} 가 각각 존재하므로 지우고 시작한다. 
    
    temp = s.split('},{') #숫자만 남기고 스플릿이 가능하다. 
    
    # len기준으로 정렬을 해주고 
    
    temp.sort(key=len)

    for i in temp: 
        tmp = i.split(',')
        for j in tmp:
            j = int(j)
            if not j in answer:
                
                answer.append(j)
    
    
    return answer


```

🤔

1. 정렬하는 과정에서 sort(key = len) 만 써도 사용이 가능하다. 
2. 파싱하는 과정에서 정규표현식을 쓰거나, 앞뒤를 제거하고 잘 나눠보자. 



---
### 3. 뉴스 클러스터링 


```python
def solution(str1, str2):
    answer = 0
    # 1. 대,소문자 구분없음. 
    # 2. 2글자씩 짜르 면서 특수문자 필터링 해야함. 
    # 3. 중복도 허용된다. 
    # 4. 값에는 65536을 곱하고 소수점자리는 버림한다. 
    # 5. 둘다 공집합일 경우에는 1 로 정의한다. 
    temp = [] # 두 글자씩 pair를 만들 자리 
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    
    for i in range(len(str1)):
        if str1[i].isalpha() and str1[i+1].isalpha(): # 알파벳이 있는 것만 넣음. 
            temp.append(str1[i:i+2])
        if i == len(str1)-2:
            break        


    temp2 = [] # str2에 대해서 위와 같이 실행 
    
    for j in range(len(str2)):
        if str2[j].isalpha() and str2[j+1].isalpha(): # 알파벳이 있는 것만 넣음. 
        
           temp2.append(str2[j:j+2])
        if j == len(str2)-2:
            break
    
    # 교집합 구하기 
    intersec = set(temp) & set(temp2)
    # 합집합 구하기 
    union = set(temp) | set(temp2)
    
    # 합집합 == 0 인것 예외처리 먼저해줌. 
    if len(union) == 0: 
        return 1*65536
    
    #자카드 구하기 
    #교집합. 

        
    jac_i = sum([min(temp.count(x), temp2.count(x)) for x in intersec])
    #합집합
    jac_u = sum([max(temp.count(y), temp2.count(y)) for y in union])

    answer = int(jac_i / jac_u * 65536)
    
    return answer

```


*다른 풀이*


```python
from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


```


🤔
1. 위에서는 set을 사용 union, intersection을 하나씩 구했다면 counter함수를 import한다하여도 구할 수 있음.
2. 두개의 합집합의 len을 예외 처리도 가능하지만, 카카오 해설을 본경우
3. except ZeroDivisionError: 의 경우처럼 예외처리를 해주는 방식을 원했던 문제같다. 




### 4. k진수에서 소수 개수 구하기 

```python
def solution(n, k):
    answer = 0
    n = change_num(n,k)
    temp = [] 
    temp = n.split('0') # 0을 기준으로 숫자가 나눠지기에 0으로 split한다면 check 해야하는 숫자만 남을듯. 
    #중간에 0이있는 숫자 역시 거를 수 있음. 
    
    for i in temp: 
        if i.isnumeric():
            i = int(i)
            if i > 1:
                if is_prime(i):
                    answer += 1
    
    return answer



def is_prime(num): # 소수인지 아닌지를 체크하는 함수. 
    flag = True
    for i in range(2, int(num**0.5)+1): # 소수 구하기 위해서 제곱근까지 search해도 된다. 
        if num % i == 0:
            flag = False
            
    return flag 
        
    
def change_num(n, k): #10진법에서 원하는 k진수로 바꾸는 방식. 
    answer = []
    while True:
        answer.append(str(n%k))
        n //= k
        if n < k:
            answer.append(str(n))
            break
            
    
    return ''.join(answer[::-1])
        
    

```



### 파일명 정렬 

1. 해당 문제의 포인트는 안전정렬이였다.
2. 기본적으로 C++ , python 은 안전정렬을 지원한다. 
3. 알고리즘 적으로는  
   > 안전정렬 : 버블 , 삽입, 병합 병렬 ... 
   > 불안정정렬: quick sort, heap sort
이 존재한다. 
![image](https://github.com/suted2/Code_prac/assets/101646531/bf461afa-35f7-4585-a3c6-0355b730e1d0)



```python
def solution(files):
    answer = []
    
    # 파일명에 포함 가능은 영어 대소문자, 숫자, 공백 , '.' , '-' 뿐이다. 
    # 파일명은 영문자로 시작하고 숫자가 최소 하나 들어있다. 
    # head -> 오직 영어 , number -> 0 ~ 99999 사이 숫자 tail 은 random 하게 존재 가능 
    # head 비교시에는 대소문자 구분하지 않는다. 
    # tail 은 정렬에 영향을 미치지 않는다. 
    
    for file in files: 
        tmp_idx = 0
        temp = []
        for i in file: # 맨처음 숫자가 나오는 부분을 number의 시작으로 보고 split하면 될듯하다.
            if i.isnumeric():
                tmp_idx = file.index(i)
                break
        # 가지고 있는 index를 기준으로 나눈다. 
        temp.append(file[:tmp_idx])
        
        ## 위에서 head부분 골랐으니 이제 number , tail 부분 구별한다. 
        tmp_idx2 = 0 
        for j in file[tmp_idx:]:
            if not j.isnumeric():
                tmp_idx2 = file.index(j)
                break
        temp.append(file[tmp_idx:tmp_idx2])
        temp.append(file[tmp_idx2:])
        
        answer.append(temp)        
    
    answer = sorted(answer, key = lambda x: (x[0].lower(), int(x[1]) ) ) 
    
    submission = [] 
    for x in answer:
        submission.append(''.join(x))
    
    
    return submission

```


🤔 

- 진행한 코드에서 head, num ,tail을 나누는 과정에서 num 의 자리수가 한정 되어있지만 예외를 처리하지 못함. 


*다른 풀이*

```python
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return temp

```

> 정규표현식으로 숫자가 [0-9] 한개 이상인 부분을 기준으로 spilt하면 3가지가 나온다. 


```python

import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d{1,5}', file.lower())[0])
    return b

```
