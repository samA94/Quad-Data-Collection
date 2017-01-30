import rospy
from sensor_msgs.msg import Imu
import time
import os

global pos_File, imu_data

rospy.init_node('IMU_Data_Capture')

imu_data = Imu()

#filename = raw_input("Please enter the desired file name, with the extension.")

filename = "data/IMU_Data1.txt"
i=1
while os.path.isfile(filename):
    i = i + 1
    filename = filename[:13] + str(i) + '.txt'


pos_File = open(filename, 'w')
pos_File.write('IMU Data Storage' + '\n')

def callback(data):
    global imu_data, pos_File

    imu_data = data
    timestamp = float(imu_data.header.stamp.secs) + float(imu_data.header.stamp.nsecs)/1000000000
    timestamp = repr(timestamp)

    pos_File.write(timestamp + ',')
    pos_File.write(str(imu_data.linear_acceleration.x) + ',')
    pos_File.write(str(imu_data.linear_acceleration.y) + ',')
    pos_File.write(str(imu_data.linear_acceleration.z) + ',')
    pos_File.write(str(imu_data.angular_velocity.x) + ',')
    pos_File.write(str(imu_data.angular_velocity.y) + ',')
    pos_File.write(str(imu_data.angular_velocity.z) + '\n')
    pos_File.flush()

rospy.Subscriber("/imu/data_raw", Imu, callback)
rospy.spin()
