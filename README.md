go to the catkin_ws folder using cd command in your terminal
type catkin_make in your terminal

to run teleop:-

enter the catkin_ws in the terminal and type the following commands:- 

source devel/setup.bash
roslaunch urdf_file template_launch.launch 

open new terminal and type:-

source devel/setup.bash
rviz

open new terminal and type:-

source devel/setup.bash
rosrun urdf_file teleop_template.py



to make the bot run in a straight line:-

enter the catkin_ws in the terminal and type the following commands:- 

source devel/setup.bash
roslaunch urdf_file template_launch.launch 

open new termianl and type:-

source devel/setup.bash
rosrun straight_line_subscriber.py

open new termianl and type:-

source devel/setup.bash
rosrun straight_line_publisher.py
