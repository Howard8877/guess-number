import random
r = random.randint(1,100)
count = 0
while True:
	g = input('1~100請猜一個整數:')
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
