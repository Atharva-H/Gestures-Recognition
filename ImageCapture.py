import cv2
import os
import uuid
import time

IMAGEPATH='Image/collectionimages'

labels=['open_pam','wrist']
numberofimg=20


for label in labels:
    #mkdir {'Images\collectionimages\\'+label}
    cap = cv2.VideoCapture(0)
    print('Collection imf for {}'.format(label))
    time.sleep(5)
    for imgnum in range(numberofimg):
        ret,frame=cap.read()
        imagename=os.path.join(IMAGEPATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
