from machine import Pin, PWM
import utime

# servo connected to GPIO 0
ledPin = Pin(13)
servo = PWM(Pin(0))

# set frequency to 50 Hz
servo.freq(50)
while True:
    # stop the servo (neutral position, pulse width of 1500us)
    pulse_width = 1500
    servo.duty_ns(pulse_width * 1000)

    # pause for 2 seconds
    utime.sleep(2)

    # make the servo rotate clockwise (pulse width of 1000us)
    pulse_width = 1000
    servo.duty_ns(pulse_width * 1000)

    # pause for a time corresponding to 90 degrees rotation
    # you will need to figure out the appropriate time for your specific servo
    utime.sleep(0.64)

    # stop the servo (neutral position, pulse width of 1500us)
    pulse_width = 1500
    servo.duty_ns(pulse_width * 1000)
    
    # wait for 24 hours
    utime.sleep(2)
