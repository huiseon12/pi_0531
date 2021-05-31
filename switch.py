#switch on -> led on
import RPi.GPIO as GPIO
Switch=10
led=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)
while True:
    if GPIO.input(Switch)==GPIO.HIGH:
        GPIO.output(led,GPIO.HIGH)
        print("push & ON")
        
    else:
        GPIO.output(led,GPIO.LOW)
        print("not push & OFF")