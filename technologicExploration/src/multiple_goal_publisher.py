#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import time
from nav_msgs.msg import Odometry
import math
from geometry_msgs.msg import (
    PoseArray,
    PoseStamped,
    Pose,
    Point,
    Twist,
    TransformStamped,
    Quaternion,
)
import numpy as np
def listener(robotsList):
	for robot for robotsList:	
		filename=robot
		filename+='_goals.txt'
		file = open(filename, 'r')

		with open(filename, 'r') as f:
    		first_line = f.readline()



		for line in file:
	    	values = line.split("\t")
	    	goal_x=float(values[0])
	    	goal_y=float(values[1])

	    	goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
		               'SUCCEEDED', 'ABORTED', 'REJECTED',
		               'PREEMPTING', 'RECALLING', 'RECALLED',
		               'LOST']
			topicName="/"
			topicName+=robotName
			topicName+="/move_base"
			move_base = actionlib.SimpleActionClient(topicName, MoveBaseAction)
			rospy.loginfo("Waiting for move_base action server...")
			move_base.wait_for_server(rospy.Duration(60))
			rospy.loginfo("Connected to move base server")
			rospy.loginfo("Starting Exploration")
			#while not rospy.is_shutdown():
			goal = MoveBaseGoal()
			goal.target_pose.pose.position.x = (goal_x)
			goal.target_pose.pose.position.y = (goal_y)
			goal.target_pose.pose.orientation.w = 1
			goal.target_pose.header.frame_id = 'map'
			goal.target_pose.header.stamp = rospy.Time.now()
			rospy.loginfo("Goal Set!")
			move_base.send_goal(goal)
			finished_within_time = move_base.wait_for_result(rospy.Duration(300)) 

			if not finished_within_time:
			    move_base.cancel_goal()
			    rospy.loginfo("Timed out achieving goal")
			else:
			    state = move_base.get_state()
			    if state == GoalStatus.SUCCEEDED:
				rospy.loginfo("Goal succeeded!")
				rospy.sleep(1)
				rotateInPlace("robot1")
				rospy.loginfo("Done!! Move to next goal!")
				else:
					rospy.loginfo("Goal failed with error code: " + str(goal_states[state]))
					rotateInPlace("robot1")
				rospy.loginfo("Goal failed!! Move to next goal!")
		file.close()
    
if __name__ == '__main__':
	print('Initialized')
    no_of_robs=sys.argv[1]
    while(counter<=int(no_of_robs)):
        rob="robot" + str(counter)
        #rotateInPlace(rob)
        robotsList.append(rob)
        print("counter   :  "+str(counter))
        counter+=1
	listener()
