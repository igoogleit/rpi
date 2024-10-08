#Pin Connection
#CLK -> 40
#DIO -> 38
#VCC -> 5v
#GND -> GND

import tm1637
from time import sleep
from datetime import datetime

tm = tm1637.TM1637(clk=21, dio=20)

while 1:
    now = datetime.now()
    hr = now.strftime('%H')
    minute  now.strftime('%M')
    tm.number(int(hr), int(minute))
    sleep(1)
