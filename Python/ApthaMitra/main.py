from machine import Pin,UART
import machine
import utime
from time import sleep
from dfplayermini import Player
led=Pin(2,Pin.OUT)

music = Player(pin_TX=17, pin_RX=16)
music.volume(20)

i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
rtc_address = 0x68

def bcd_to_decimal(val):
    return (val >> 4) * 10 + (val & 0x0F)

def rtct():
    data = i2c.readfrom_mem(rtc_address, 0, 7)
    seconds = bcd_to_decimal(data[0] & 0x7F)
    minutes = bcd_to_decimal(data[1] & 0x7F)
    hours = bcd_to_decimal(data[2] & 0x3F)
    print("RTC time set manually to:", " {} {}".format(hours, minutes))
    return hours,minutes
while True:
    hour=rtct()[0]
    minute=rtct()[1]
    print(hour,minute)
    hlist=[5,14,14,14,14]
    mlist=[0,2,3,5,8]
    for i in range(0,4,1):
        if hlist[i]==hour and mlist[i]==minute:
            led.value(1)
            music.play(i+1)
            sleep(5)
            led.value(0)
        #deepsleep(1000*60*int(interval1)*int(interval))#in milisecons
    utime.sleep(60)

