from math import floor, ceil, sqrt

def solution(r1, r2):
    dot = 0
    
    # x좌표 1~r2까지 각 x값에서 두 원 사이에 포함된 y값 찾기
    for i in range(1, r2+1):
        max_y = floor(sqrt(r2**2 - i**2))
        min_y = 0 if i > r1 else ceil(sqrt(r1**2 - i**2))
        
        dot += max_y - min_y + 1
    

    return dot * 4