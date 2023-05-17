# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

# 여러줄 입력 시 효율성을 좋게 하기위해 input() 대신 sys.stdin.readline()를 사용
input = sys.stdin.readline

n, m = map(int, input().split())
input_nums = []

cards = {key: 0 for key in range(1, n+1)}
queue = []

count = 0

# input_nums[]에 m개의 숫자를 입력 받음
for i in range(m):
	input_nums.append(int(input()))

# Timeout이 안나게 하기 위해 for문 안에서 in 조건문이나 index() 메서드를 사용하지 않고 딕셔너리(cards), 리스트(queue)를 활용해 모은 카드의 번호를 체크
for num in input_nums:
	# 중복되지 않게 모은 카드 번호 갯수가 n(최대 번호)와 같으면 break
	if len(queue) == n:
		break
		
	else: 
		count += 1
		
		# 모으지 않은 카드라면 cards[num] == 0  ->  cards[num] == 1로 바꿔주고, queue에 해당 카드 번호를 넣는다.
		if cards[num] == 0:
			cards[num] = 1
			queue.append(num)
	

if len(queue) < n:
	print(-1)
else:
	print(count)
	

	