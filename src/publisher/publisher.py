#!/usr/bin/env python

import math
import rospy
from sensor_msgs.msg import Image
from PIL import Image as PIL_Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

def publishImage(publisher, file_name):
  print (publisher)
  if publisher is None:
      return
  
  image_data = PIL_Image.open(file_name)
  image_data = np.asarray(image_data)
  image_ros_message = CvBridge().cv2_to_imgmsg(image_data, encoding="rgb8")
  print ("publishing")
  publisher.publish(image_ros_message)

def image_publisher():
  publisher = rospy.Publisher('/image_publisher', Image, queue_size=10)
  print (publisher)
  rospy.init_node('image_publisher')
  rate = rospy.Rate(0.1)
  start_time = 0

  while not start_time:
    start_time = rospy.Time.now().to_sec()

  while not rospy.is_shutdown():
    elapsed = rospy.Time.now().to_sec() - start_time
    print("foo")
    publishImage(publisher, 'test.png')
    rate.sleep()

if __name__ == '__main__':
  try:
    image_publisher()
  except rospy.ROSInterruptException:
    pasS
