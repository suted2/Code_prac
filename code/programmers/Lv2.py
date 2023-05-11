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
