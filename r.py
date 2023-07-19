import random
start = input('請輸入開始值:')
end = input('請輸入結束值')
print('---------------------------------------')
start = int(start)
end = int(end)
answer = random.randint(start, end)
count = 0
while True:
	print(start, '~', end)
	guess = input('請猜1個數字:')
	guess = int(guess)
	count += 1
	if guess == answer:
		print('猜對了!')
		print('你總共猜了', count, '次')
		break
	elif guess > answer:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次')
	print('---------------------------------------')	


