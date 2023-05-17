def solution(targets):
    sortedTargets = sorted(targets, key=lambda x: x[1])
    
    system_end = 0
    count = 0
    
    for target in sortedTargets:
        if target[0] < system_end:
            continue
        else:
            system_end = target[1]
            count += 1
    
    return count
