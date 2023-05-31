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
