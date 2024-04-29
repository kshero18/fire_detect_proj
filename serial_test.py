import serial
import RPi.GPIO as GPIO

data = serial.Serial(
                 '/dev/ttyS0',
                   baudrate = 9600,
                    parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
 #                   )
                    timeout=1 # must use when using data.readline()
                    )


GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.LOW)

GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)


while True:

    x = data.read(1)
    x=x.decode('UTF-8','ignore')

    if x=='1':
        print('Light On')
        GPIO.output(2, GPIO.HIGH)
    if x=='2':
        print('Fan on')
        GPIO.output(3, GPIO.HIGH)

    if x=='3':
        print('Tv On')
        GPIO.output(4, GPIO.HIGH)
    if x=='4':
        print('led on')
        GPIO.output(17, GPIO.HIGH)

    if x=='5':
        print('Light off')
        GPIO.output(2, GPIO.LOW)
    if x=='6':
        print('Fan off')
        GPIO.output(3, GPIO.LOW)

    if x=='7':
        print('Tv off')
        GPIO.output(4, GPIO.LOW)
    if x=='8':
        print('led off')
        GPIO.output(17, GPIO.LOW)
    
