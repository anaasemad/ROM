import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anaase_linux/RM_prac/install/turtlebot3_dqn'
