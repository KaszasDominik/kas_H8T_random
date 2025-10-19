# array_sorter

A **ROS 2 Humble** kompatibilis package, amely egy egyszerű Python node-ot tartalmaz.  
Ez a node feliratkozik egy `std_msgs/msg/Float32MultiArray` típusú topicra, amely bemeneti lebegőpontos tömböt tartalmaz, majd közzéteszi a tömb **növekvő sorrendbe rendezett** változatát.

---

## Features

- Feliratkozás a `/input_array` topicra (`Float32MultiArray` típusban)  
- Beérkező tömb rendezése növekvő sorrendben  
- Rendezett tömb publikálása a `/sorted_array` topicon  
- Egyszerű, robusztus node implementáció Pythonban ROS 2 Humble alatt  

---

## Packages and Build

### Workspace elvárás
Feltételezzük, hogy a ROS 2 workspace a következő helyen található:
~/ros2_ws/


### Clone the package
cd ~/ros2_ws/src
git clone https://github.com/KaszasDominik/kas_H8T_random

### Build the package
cd ~/ros2_ws
colcon build --packages-select array_sorter --symlink-install


### Source the workspace
Ne felejtsd el forrásolni a workspace-t:
source ~/ros2_ws/install/setup.bash


---

## Run the Node

### Launch fájlon keresztül:
ros2 launch array_sorter launch_array_sorter.launch.py


### Vagy közvetlenül futtatva:
ros2 run array_sorter_pkg array_sorter

---

## Check Operation

A működés ellenőrzéséhez használd az alábbi parancsokat:

**Bemeneti, nem rendezett tömb megtekintése:**
ros2 topic echo /input_array


**Kimeneti, rendezett tömb megtekintése:**
ros2 topic echo /sorted_array


---

## License

Ez a projekt oktatási és demonstrációs céllal készült.

