import cv2
from udpclient import img_to_ascii
from PIL import Image
import numpy

live = cv2.VideoCapture(0)
while True:
    ret, frame = live.read()
    print(ret)
    ascii_frame = numpy.array(img_to_ascii(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))))
    cv2.imshow('frame', ascii_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


