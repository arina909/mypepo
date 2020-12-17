mytime = input()
time = float('.'.join(mytime.split(':')))
eqiv = 90/(12-6)/60
# find how many minutes in one sun angle
if time > 6.00 and time < 18.00:
    reltime = time-6.00
    # start counting from 6.00
    minutes = reltime // 1 * 60 + reltime % 1 * 100
    # convert hours into minutes
    sun_angel = minutes*eqiv
    print('%.2f' % sun_angel)
else:
    print('I don\'t see the sun!')