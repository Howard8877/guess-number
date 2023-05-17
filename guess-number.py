import random
start = input('請輸入隨機數字開始值:')
end = input('請輸入隨機數字結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	g = input('請猜一個整數:')
	g = int(g)
	count += 1
	if g == r:
		print('你猜對了!')
		print('你猜了', count,'次')
		break
	elif g > r:
		print('比答案大')
	elif g < r:	
		print('比答案小')
	print('這是你猜的第', count, '次')
