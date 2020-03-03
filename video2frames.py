import cv2
import argparse
import time
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True, help="directory to video")
ap.add_argument("-o", "--output", type=str, required=True, help="directory to output frames")
ap.add_argument("-s", "--skip", type=int, default=15, help="no of frames to skip")

args = vars(ap.parse_args())

INPUT_PATH = args["input"]
OUTPUT_PATH = args["output"]
FRAMESTOSKIP = args["skip"]


vidcap = cv2.VideoCapture(INPUT_PATH)
success,image = vidcap.read()
count = 0
success = True
while success:
  #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  if count % FRAMESTOSKIP ==0:
  	cv2.imwrite(OUTPUT_PATH + "/%s_%d.jpg" %(time.time(),count), image)     # save frame as JPEG file
  success,image = vidcap.read()
  count+=1  


