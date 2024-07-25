# Video Demonstration
![video_demo](https://github.com/user-attachments/assets/38844afb-68b1-4473-9b1a-57e224609da3)

# Building and running
```git clone https://github.com/unitreerobotics/unitree_legged_sdk.git ```<br>
Add the following 2 lines to CMakeLists.txt: <br>
```add_executable(run example/run.cpp)``` <br>
```target_link_libraries(run ${EXTRA_LIBS}) ```<br>
```git clone https://github.com/colemaring/go1-project.git ```<br>
Move run.cpp into examples folder <br>
cd build and compile. you'll need [these dependencies](https://github.com/colemaring/go1-project/blob/main/dependencies). <br>
```cmake .. && make``` <br>
Connect to Go1's network. Password is 00000000 <br>
run with ./run <br>
Now run main.py<br>

# Resources 
cmd modes: https://unitree-docs.readthedocs.io/en/latest/get_started/Go1_Edu.html <br>
