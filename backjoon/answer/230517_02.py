import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x, y):
  queue = []
  queue.append([x, y])

  visited[x][y] = True

  while queue:
    now = queue.pop(0)

    for i in range(4):
      newX = now[0] + dx[i]
      newY = now[1] + dy[i]

      if newX < 0 or newX >= n or newY < 0 or newY >= m:
        continue
      
      if arr[newX][newY] == 0 or visited[newX][newY] == True:
        continue

      if arr[newX][newY] == 1:
        visited[newX][newY] = True

        arr[newX][newY] = arr[now[0]][now[1]] + 1
        queue.append([newX, newY])
  
  return arr[n-1][m-1]

print(bfs(0,0))

