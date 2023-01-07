import time
import datetime

from libdev.cfg import cfg

from lib.vk import read, send, info


tzinfo=datetime.timezone(datetime.timedelta(hours=cfg('tz')))

while True:
    timestamp = time.time()
    current_time = datetime.datetime.fromtimestamp(timestamp, tz=tzinfo)

    if current_time.weekday() < 5 and (
        9 < current_time.hour < 18
        or (current_time.hour == 9 and current_time.minute > 40)
        or (current_time.hour == 18 and current_time.minute < 30)
    ):
        time.sleep(300)
        continue

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
        name = info(i[0]).get('name', 'Привет')

        if current_time.weekday() >= 5:
            send(i[0], cfg('message2').format(name))
            continue

        send(i[0], cfg('message1').format(name))

    time.sleep(120)
