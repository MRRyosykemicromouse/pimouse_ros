#!/usr/bin/env python
import sys, rospy
from pimouse_ros.msg import LightSensorValues

if __name__ == '__main__':
    #freq = 10
    #if rospy.has_param('lightsensors_freq'):
    #freq = rospy.get_param('lightsensors_freq',10)
        
    devfile = '/dev/rtlightsensor0'
    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        try:
            with open(devfile,'r') as f:
                data = f.readline().split()
                d = LightSensorValues()
                d.right_forward = int(data[0])
                d.right_side = int(data[1])
                d.left_side = int(data[2])
                d.left_forward = int(data[3])
                #d.sum_all = sum(data)
                d.sum_forward = int(data[0]) + int(data[3])
                pub.publish(d)
        except IOError:
            rospy.logerr("cannot write to  " + devfile)

        rate.sleep()

