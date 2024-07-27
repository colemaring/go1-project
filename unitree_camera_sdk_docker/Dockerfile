FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get upgrade -y

RUN apt install -y git build-essential libboost-all-dev cmake freeglut3-dev libudev-dev libopencv-dev

RUN git clone https://github.com/unitreerobotics/UnitreecameraSDK.git

WORKDIR /UnitreecameraSDK

RUN mkdir build

WORKDIR build

RUN cmake ..

RUN make
