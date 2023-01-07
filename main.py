import time

from lib.vk import read, send


while True:
	try:
		new_message = read()

	except:
		print('Ошибка чтения!')
		time.sleep(5)

	else:
		for i in new_message:
			send(i[0], 'чё надо')

	time.sleep(120)
