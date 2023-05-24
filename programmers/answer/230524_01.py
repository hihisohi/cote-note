def solution(plans):
    answer = []
    stack = []
    
    # 시, 분을 통합하여 int로 변경
    for plan in plans:
        h, m = plan[1].split(':')
        plan[1] = int(h) * 60 + int(m)
        plan[2] = int(plan[2])
    
    # 시작 시간으로 정렬
    sorted_plans = sorted(plans, key=lambda x:x[1])

    
    for name, start, playtime in sorted_plans:
        
        # stack이 비어있으면 stack에 과제를 넣고 다음 순서로 넘어감
        if not stack:
            stack.append([name, start, playtime])
            continue
        
        # stack[-1]인 과제가 현재 해야하는 과제
        _, cur_start, _ = stack[-1]
        
        working_time = start - cur_start
        
        while working_time > 0 and stack:
            cur_name, cur_start, cur_playtime = stack.pop()
            
            if cur_playtime > working_time:
                stack.append([cur_name, cur_start, cur_playtime - working_time])
                break
            else:
                working_time -= cur_playtime
                answer.append(cur_name)
        
        stack.append([name, start, playtime])
        
        
    
    # 시작 시간 순서로 마지막 과제까지 다 탐색하고 stack에 남은 멈춰있는 과제가 있으면 뒤에부터 차례대로 반환
    while stack:
        stacked_name, _, _ = stack.pop()
        answer.append(stacked_name)
        
    return answer