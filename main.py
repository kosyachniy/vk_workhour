import time
import datetime

from libdev.cfg import cfg

from lib.vk import read, send


tzinfo=datetime.timezone(datetime.timedelta(hours=cfg('tz')))

while True:
    try:
        new_message = read()

    except Exception as e:
        print('Error', e)
        time.sleep(60)
        continue

    for i in new_message:
        message_time = datetime.datetime.fromtimestamp(i[3], tz=tzinfo)
        print(message_time.hour, message_time.minute)
        send(i[0], 'чё надо')

    time.sleep(120)
