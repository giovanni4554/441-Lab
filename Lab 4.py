import RPi.GPIO as GPIO
import time # import time.sleep()
import math

GPIO.setmode(GPIO.BCM) # use BCM port numbering
p = [4,5,6,7] # pin number
            #i=range(len(p))
frequency_Hz = 500
    
ctr=0

while True:
    
    f=0.2
    t = time.time()
    for pin in p:
        GPIO.setup(pin, GPIO.OUT) # assign the pin as output
        pwm = GPIO.PWM(pin, frequency_Hz) # create a PWM object
        pwm.start(0) # set duty cycle (0.0 – 100.0)
      
        duty_cycle=100*pow(math.sin(2*math.pi*t*f),2)
        #pwm.ChangeDutyCycle(duty_cycle) # change duty cycle (0.0 – 100.0)
    #pwm.stop()
    #GPIO.output(p, 0) # set output to 0V