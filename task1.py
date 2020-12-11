s = input()
l = s.split(':')
t = float('.'.join(l))
eq=90/(12-6)/60
# find how many minutes in one sun angle
if t > 6.00 and t < 18.00:
    t1 = t-6.00
    # start counting from 6.00
    m = t1 // 1 * 60 + t1 % 1 * 100
    # convert hours into minutes
    sun_angel = m*eq
    print('%.2f' % sun_angel)
else:
    print('I don\'t see the sun!')