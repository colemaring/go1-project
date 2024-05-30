# Dependencies
[Docker](https://www.docker.com/get-started/) <br>
Git <br>

Ensure the docker engine is running before running these commands. <br>

# Building the images
 - May take a while depending on computer speed <br>
```git clone https://github.com/colemaring/go1-docker.git ```<br>
```cd go1-docker/unitree_legged_sdk && docker build -t unitree_legged_sdk_image .```  <br>
```cd go1-docker/unitree_camera_sdk && docker build -t unitree_camera_sdk_image .```  <br>
```cd go1-docker/unitree_legged_sdk_python && docker build -t unitree_legged_sdk_image_python .```  <br>

# Running the images
-power on and connect to the Go1's wifi network. Password is 00000000 <br>
```docker run -it unitree_legged_sdk_image```  <br>
```docker run -it unitree_camera_sdk_image```  <br>

# Running the examples in the container
connect to Go1 over wifi and ensure your ipv4 is set to the specified value? -im not sure if this is needed for now <br>
For legged SDK <br>
```./example_walk``` <br>

For camera SDK <br>
```cd .. && cd bins ``` <br>
```./example_getRawFrame``` <br>

# Resources
TODO: <br>
Robot modes: https://unitree-docs.readthedocs.io/en/latest/get_started/Go1_Edu.html <br>
add python build option as a tag <br>
