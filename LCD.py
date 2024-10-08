#16x2 LCD
#configuration
#Step 1: Preference --> Raspberry pi Configuratoin --> Interfaces --> Enable i2c

##Note: Disable SPI if its enabled

#Step 2: Open Treminal
#cd Desktop
#mkdir LCD
#sudo i2cdetect -y 1

##Note: Check Channel Number and remember it

#Pin Connection
#RPI -> i2c
#3 -> SDA
#4 -> VCC
#5 -> SCL
#6 -> GND

#Step 3: Open Thony/Genny IDE to write a code

from time import sleep
from RPLCD.i2c import charLCD

lcd=charLCD(i2c_expander='PCF8574',address=0x27,port=1,cols=16,rows=2,datsize=8)

lcd.clear()
lcd.write_string(str("Hello Guys"))
   
