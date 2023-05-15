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
