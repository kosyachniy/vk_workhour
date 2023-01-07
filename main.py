import time
import datetime

from libdev.cfg import cfg

from lib.vk import read, send


tzinfo=datetime.timezone(datetime.timedelta(hours=cfg('tz')))

while True:
    timestamp = time.time()

    try:
        new_message = read()

    except Exception as e:
        print('Error', e)
        time.sleep(60)
        continue

    for i in new_message:
        if timestamp - i[3] < cfg('delay'):
            continue

        message_time = datetime.datetime.fromtimestamp(i[3], tz=tzinfo)

        if message_time.weekday() < 5 and (
            9 < message_time.hour < 18
            or (message_time.hour == 9 and message_time.minute > 30)
            or (message_time.hour == 18 and message_time.minute < 30)
        ):
            continue

        send(i[0], 'чё надо')

    time.sleep(120)
