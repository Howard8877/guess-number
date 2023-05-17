import random
r = random.randint(1,100)
while True:
	g = input('1~100請猜一個整數:')
	g = int(g)
	if g == r:
		print('你猜對了!')
		break
	elif g > r:
		print('比答案大')
	elif g < r:	
		print('比答案小')





