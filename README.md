# ROS Publish/Subscribe Example

## Building
run `catkin_make`

## Running
### Start ROS Core
```
$ roscore
```

### Start the Image publisher
```
$ source devel/setup.bash
$ rosrun publisher publisher.py 
```

### Start the Image subscriber
```
$ source devel/setup.bash
$ rosrun subscriber subscriber.py 
```
