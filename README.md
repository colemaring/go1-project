# Dependencies
Docker

# Building the images
git clone this repo <br>
cd into the sdk that you want to build <br>
docker build -t unitree_legged_sdk_image . <br>
docker build -t unitree_camera_sdk_image . <br>

# Running the images
docker run -it unitree_legged_sdk_image <br>
docker run -it unitree_camera_sdk_image <br>


