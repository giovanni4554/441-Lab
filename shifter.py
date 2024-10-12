import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Shifter:
    def __init__(self, dataPin, clockPin, latchPin):
        self.dataPin=dataPin
        self.clockPin=clockPin
        self.latchPin=latchPin
        
        
    def __ping(self,p):
        GPIO.output(p,1)
        time.sleep(0.001)
        GPIO.output(p,0)
        
    def shiftByte(self, b): # send a byte of data to the output
        for i in range(8):
            GPIO.output(self.dataPin, b & (1<<i))
            self.__ping(self.clockPin) # add bit to register
        self.__ping(self.latchPin) # send register to output
        
    


dataPin, latchPin, clockPin = 23, 24, 25

s1 = Shifter(dataPin, clockPin, latchPin)



GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)  # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)  

pattern = 0b11111111        # 8-bit pattern to display on LED bar

s1.shiftByte(pattern)

try:
  while 1: pass
except:
  GPIO.cleanup()