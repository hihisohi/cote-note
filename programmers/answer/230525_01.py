def solution(name, yearning, photo):
    answer = []
    
    name_yearning = {key: value for key, value in zip(name, yearning)}
    
    for p in photo:
        result = 0
        
        for i in p:
            if i in name_yearning.keys():
                result += name_yearning[i]
        
        answer.append(result)
        
    return answer