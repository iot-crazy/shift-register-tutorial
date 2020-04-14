from machine import Pin
from time import sleep

rclk = Pin(4, Pin.OUT)
ser = Pin(2, Pin.OUT)
srclk = Pin(5, Pin.OUT)

rclk.value(0)
ser.value(0)
srclk.value(0)

def sendbit(bit):
    srclk.value(0)
    ser.value(bit)
    srclk.value(1) 

def sendbyte(data):
    bitmask = int('00000001', 2)
    for i in range(8):
        sendbit(int(bitmask & data))
        data = data >> 1
    rclk.value(1)
    rclk.value(0) 

seq1 = [1,2,4,8,16,32,64,128,64,32,8,4,2]
seq2 = [0xAA, 0x55]

while True:
    for t in range(10):
        for i in seq1:
            print(i)
            sendbyte(i)
            sleep(0.1)
    for t in range(20):
        for i in seq2:
            sendbyte(i)
            sleep(0.2)
            