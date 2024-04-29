import cv2
import numpy as np
import serial
import atttachem

from twilio.rest import Client


data = serial.Serial(
                 '/dev/ttyS0',
                   baudrate = 9600,
                    parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE,
                   bytesize=serial.EIGHTBITS,
 #                   )
                    timeout=1 # must use when using data.readline()
                    )

### Find these values at https://twilio.com/user/account
account_sid = "AC59c1a7238efd97b6b15b218e3d79f08f"
auth_token = "a0f0386d29f71030f11e0b7a995d7ad9"

client = Client(account_sid, auth_token)
mon=0
 
#video_file = "video_1.mp4"
video = cv2.VideoCapture(0)
 
while True:
    print('waiting ')
    x = data.read(1)
    x=x.decode('UTF-8','ignore')

    if x=='1':
        mon=1
        print('Fire from sensor open camera')
        

    while mon==1:
        (grabbed, frame) = video.read()
        if not grabbed:
            break
     
        blur = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
     
        lower = [18, 50, 50]
        upper = [35, 255, 255]
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv, lower, upper)
        
     
     
        output = cv2.bitwise_and(frame, hsv, mask=mask)
        no_red = cv2.countNonZero(mask)
        cv2.imshow("output", output)
       
        #print("output:", frame)
        if int(no_red) > 20000:
            print ('Fire detected')
            cv2.imwrite('frame.png',output)
            mon=0
            client.api.account.messages.create(
        to="+91-6362101806",
        from_="+12029294795" ,  #+1 210-762-4855"
        body='FIRE DETECTED at http://www.google.com/maps/?q={},{}'.format('12.8865','77.4498'))
            
            atttachem.sendMail( ["ksrksheeraja@gmail.com"],
             "Fire detcted",
            "this is the body text of the email",
            ["frame.png","text.txt"] )
        #print(int(no_red))
       #print("output:".format(mask))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
cv2.destroyAllWindows()
video.release()
