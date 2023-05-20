def solution(sequence, k):
    answer = [0, 0]
    sum_list = [0]
    
    for i in range(0, len(sequence)):
        sum_list.append(sum_list[i] + sequence[i])
    
    start = 1
    end = len(sequence)
    idx = 1
    answer_list = []
    
    while start <= end:
        if sum_list[start] - sum_list[idx-1] < k:
            start += 1
        elif sum_list[start] - sum_list[idx-1] == k:
            answer_list.append([idx-1, start-1])
            idx += 1
            start += 1
        else:
            idx += 1
    
    answer = answer_list[0]
    
    if len(answer_list) == 1:
        return answer
        
    diff = answer_list[0][1] - answer_list[0][0]
    for i in answer_list:
        if i[1] - i[0] < diff:
            diff = i[1] - i[0]
            answer = i
 
    return answer