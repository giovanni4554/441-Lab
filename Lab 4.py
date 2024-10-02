import RPi.GPIO as GPIO
import time  # import time.sleep()
import math

GPIO.setmode(GPIO.BCM)
# use BCM port numbering
p = [4, 17, 27,22, 10, 9,11, 5 ,6, 13]  # pin number
frequency_Hz = 500

ctr = 0

while True:

    f = 0.2
    t = time.time()
    for pins in p:
        GPIO.setup(p, GPIO.OUT)
          # assign the pin as output
        pwm = GPIO.PWM(pins, frequency_Hz)  # create a PWM object
        pwm.start(0)  # set duty cycle (0.0 – 100.0)

        duty_cycle = 100 * pow(math.sin(2 * math.pi * t * f), 2)
        pwm.ChangeDutyCycle(duty_cycle) # change duty cycle (0.0 – 100.0)
        pwm.stop()
        GPIO.output(pins, 0) # set output to 0V
