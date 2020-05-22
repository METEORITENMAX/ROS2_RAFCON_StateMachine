# ROS2 RAFCON StateMachine

Integration of ros2 into a rafcon StateMachine. The StateMachine shows an example for a Publisher and a Subscriber with and without a class.

Tested on:
- Ubuntu 18.04
- ROS eloquent

### Rafcon Installtion

Install Rafcon via pip3, because ros2 is using python3.
```
pip3 install rafcon
```

Some libraries might missing like `libgirepository1.0-dev`.


## Usage
Start `rafcon` via the terminal to load necessary `ros2` environment variables.
Open the State Machine in `rafcon`.

Publish a Message to `topic` by:
```
ros2 topic pub /topic std_msgs/msg/String "data: Hello World"
```
 to finish the Subscriber State.


### Notes
The StateMachine should consist of exactly one ros node. Therefore the `init_ros_node` library state was rewritten to initialize a ros2 node. The new `init_ros2_node` must be placed at the beginning of each StateMachine to use ros2 functionalities.
