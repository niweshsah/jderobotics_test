# ROS 2 Workspace: Publisher-Subscriber & Navigation

## Part 1: ROS 2 Publisher-Subscriber

### 1. Clone the Repository
```bash
git clone https://github.com/niweshsah/jderobotics_test.git ~/ros2_ws/src/my_talker
cd ~/ros2_ws
```

### 2. Build the Package
```bash
colcon build
source install/setup.bash
```

### 3. Run the Nodes
Open two terminals:

**Terminal 1 (Publisher):**
```bash
ros2 run my_talker publisher
```

**Terminal 2 (Subscriber):**
```bash
ros2 run my_talker subscriber
```

---

## Part 2: Robot Launch & Navigation2

### 1. Choose and Install a ROS 2 Robot (TurtleBot3 Example)
```bash
sudo apt update && sudo apt install ros-humble-turtlebot3* ros-humble-navigation2 ros-humble-nav2-bringup
```

### 2. Launch the TurtleBot3 Simulation in Gazebo
```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

### 3. Visualize Laser Scan Data in RViz2
Open another terminal:
```bash
ros2 launch turtlebot3_bringup rviz2.launch.py
```

### 4. Perform Waypoint Navigation
1. Start the Navigation Stack:
    ```bash
    ros2 launch nav2_bringup bringup_launch.py use_sim_time:=True
    ```
2. Use the **Nav2 Goal Tool** in RViz to set at least 3 waypoints for navigation.
3. Observe the TurtleBot3 following the waypoints in simulation.


