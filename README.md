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

Open the State Machine in `rafcon`.

Publish a Message to `topic` by:
```
ros2 topic pub /topic std_msgs/msg/String "data: Hello World"
```
