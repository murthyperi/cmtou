import time
import io
import os
from cmtoUtils import is_sku
from dbOperations import insertHH
from picamera import PiCamera
from gpiozero import MotionSensor

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

pir =MotionSensor(4)
camera = PiCamera()
camera.brightness=70
camera.sharpness=70
camera.crop = (0.25, 0.25, 0.5, 0.5)
counter=1
while True:
    if pir.motion_detected:
   #     print("Motion Detected")
        camera.start_preview()
        time.sleep(10)
        camera.capture('/home/pi/Pictures/cmtou/image%s.jpg' % counter)
        camera.stop_preview()
        file_name=os.path.join(os.path.dirname(__file__), '/home/pi/Pictures/cmtou/image%s.jpg' % counter)
       # Loads the image into memory
        camera.stop_preview()
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            image = types.Image(content=content)


# Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

	    textResponse = client.text_detection(image=image)
	    texts = textResponse.text_annotations

            #print('Labels:')
            #for label in labels:
            #    print(label.description)    
            

	    print('Texts:')
	    for text in texts:
	     if(is_sku(text.description)):
	      #print('\n"{}"'.format(text.description)) 
	      # call the method to insert sku into the database
	      print("calling cloud sql")
	      insertHH(4,text.description)
	      print("success") 
	      break
        counter=counter+1
    else:
        camera.stop_preview()
    
