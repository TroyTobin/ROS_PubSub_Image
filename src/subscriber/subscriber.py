#!/usr/bin/env python

import math
import rospy
from sensor_msgs.msg import Image
from PIL import Image as PIL_Image
from cv_bridge import CvBridge, CvBridgeError
import matplotlib.pyplot as plt

subscriber = None

def subscribeImageCb(img):
  image_data = CvBridge().imgmsg_to_cv2(img, "rgb8")
  print "got new image"
  plt.imshow(image_data)
  plt.show()

def image_subscriber():
  subscriber = rospy.Subscriber('/image_publisher', Image, subscribeImageCb, queue_size=10)
  rospy.init_node('image_subscriber')
  rospy.spin()
  
if __name__ == '__main__':
  try:
    image_subscriber()
  except rospy.ROSInterruptException:
    pasS
