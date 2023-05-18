def solution(players, callings):
    temp = {name: idx for idx, name in enumerate(players)}
    
    for name in callings:
        n = temp[name]
        
        temp[players[n]] = n - 1
        temp[players[n-1]] = n
        
        players[n], players[n-1] = players[n-1], players[n]
    
    return players