# ROS 2 Turtlesim – Multi-Turtle Movement Synchronisation

A ROS 2 project demonstrating service-based turtle spawning and velocity synchronisation between two turtles using the Turtlesim simulator.

The project creates a second turtle using the `/spawn` service and makes it replicate the velocity commands received by the first turtle.

**ROS 2 Version:** Humble

---

## Concepts Used

* Python
* `rclpy`
* `turtlesim/srv/Spawn`
* `geometry_msgs/Twist`
* ROS 2 Service Clients
* Publishers
* Subscribers
* Topics
* Asynchronous Service Calls
* Multi-Robot Coordination

---

## Features

* Creates a service client to communicate with the `/spawn` service.
* Spawns a second turtle named `turtle2` at specified coordinates.
* Subscribes to `/turtle1/cmd_vel` to receive velocity commands from the first turtle.
* Extracts linear and angular velocity values from the received `Twist` message.
* Publishes the same velocity commands to `/turtle2/cmd_vel`.
* Enables the second turtle to replicate the movement commands of the first turtle.
* Uses asynchronous service communication to request turtle creation.

---

## System Design

| Create Turtle Node | ROS 2 Interface | Turtlesim |
|---|---|---|
| Creates a Service Client | `/spawn` | Spawns turtle2 |
| Creates a Subscription | `/turtle1/cmd_vel` | Receives turtle1 velocity commands |
| Creates a Publisher | `/turtle2/cmd_vel` | Sends velocity commands to turtle2 |
| `get_turtle1()` | → | Transfers velocity information |

---

## How to Run

1. Build the workspace.

```bash
colcon build
```

2. Source the workspace.

```bash
source install/setup.bash
```

3. Start the Turtlesim simulator.

```bash
ros2 run turtlesim turtlesim_node
```

4. Open a new terminal, source the workspace again, and run the turtle spawning node.

```bash
source install/setup.bash
ros2 run <package_name> <executable_name>
```

5. Open another terminal and start the keyboard teleoperation node.

```bash
ros2 run turtlesim turtle_teleop_key
```

6. Use the arrow keys to control the first turtle and observe the second turtle replicating its velocity commands.

---

## Notes

* Ensure `package.xml` and `setup.py` are updated with the correct dependencies, package name, and executable name before building the workspace.
* The second turtle replicates velocity commands rather than following the exact position or trajectory of the first turtle.
* Both turtles operate independently, with the second turtle receiving the same velocity commands as the first.
