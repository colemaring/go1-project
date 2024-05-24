# Dependencies
[Docker](https://www.docker.com/get-started/) <br>
Git <br>

# Building the images
```git clone https://github.com/colemaring/go1-docker.git ```<br>
```cd unitree_legged_sdk && docker build -t unitree_legged_sdk_image .```  <br>
OR <br>
```cd unitree_camera_sdk && docker build -t unitree_camera_sdk_image .```  <br>

# Running the images
```cd unitree_legged_sdk && docker run -it unitree_legged_sdk_image```  <br>
```cd unitree_camera_sdk && docker run -it unitree_camera_sdk_image```  <br>

# Running the examples in the container
connect to Go1 over wifi and ensure your ipv4 is set to the specified value? -im not sure if this is needed for now <br>
```./example_walk``` <br>
