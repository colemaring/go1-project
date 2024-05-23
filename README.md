# Dependencies
Docker

# Building the images
git clone this repo
cd into the sdk that you want to build
docker build -t unitree_legged_sdk_image .
docker build -t unitree_camera_sdk_image .

# Running the images
docker run -it unitree_legged_sdk_image
docker run -it unitree_camera_sdk_image


