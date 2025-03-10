#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import String, Float32
from sensor_msgs.msg import LaserScan
from lab2.msg import ScanRange


class LaserScanNode():
    def __init__(self):
        
        # create a publisher handle to publish ScanRange messages to the 
        # laserscan_range topic. Make sure you use self.var_name = xyz so
	    # that you are able to use this handle in your other functions
       	#TODO: CREATE PUBLISHER HANDLER HERE
        self.pub = rospy.Publisher('laserscan_range', ScanRange, queue_size=10)
        self.scan_range = ScanRange()
        
        # subscriber handle for the scan message. This handle 
        # will subscribe to scan and recieve LaserScan messages. Each
        # time this happens the scan_callback function is called
        rospy.Subscriber('scan', LaserScan, self.scan_callback)
        
        # initialize and register this node with the ROS master node
        rospy.init_node('laserscan_listen', anonymous=False)
        
        # Create an instance of the scan range message to store your closest and farthest
        # points. Remember, these attributes can be accesed with:
        # self.scan_range.closest_point. Also note the attributes are set to default values
        # currently.
       	#TODO: CREATE INSTANCE OF ScanRange HERE
        # I put it above with self.pub because indentation kept causing problems

    
    # this is the callback for the scan message. 
    # here we will use the scan_data parameter to access the ranges 
    # from the LaserScan message and figure out the closest and farthest point
    def scan_callback(self, scan_data):
        # Write code to loop through the laser scan ranges and find the closest
        # and farthest values. Store those values in the ScanRange instance you created
        # in __init__()
        # TODO: FILTER DATA
        minRange = scan_data.ranges[0]
        maxRange = scan_data.ranges[0]
        for i in scan_data.ranges:
            if i > scan_data.range_min and i < scan_data.range_max and i != np.nan and i != np.inf:
                if i < minRange:
                    minRange = i
                if i > maxRange:
                    maxRange = i
        # TODO: FIND CLOSEST AND FARTHEST POINTS
        self.scan_range.closestRange = minRange
        self.scan_range.farthestRange = maxRange
        pass

    # the publish method is  called on an interval in the main
    # loop of this file. This is where we publish our ranges to 
    # the topic. 
    def publish(self):
        # TODO: ADD PUBLISHER CODE HERE
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(self.scan_range)
            rate.sleep()

        pass
        

if __name__ == '__main__':
    ls = LaserScanNode()

    rate = rospy.Rate(10) # 10hz
    try:
        # Add a while loop which calls the publish() function of the laser scan node
        # on the interval we have defined with rate
        # TODO: CREATE PUBLISHER LOOP HERE 
        print("Starting laserscan_ranges")
        ls.publish()
        pass
    except rospy.ROSInterruptException:
        pass
