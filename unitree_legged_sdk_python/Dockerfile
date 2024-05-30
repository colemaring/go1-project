FROM ubuntu

RUN apt-get update && apt-get upgrade -y

RUN apt install -y wget git build-essential libboost-all-dev cmake libmsgpack-dev

RUN wget https://sourceforge.net/projects/boost/files/boost/1.54.0/boost_1_54_0.tar.gz/download -O boost_1_54_0.tar.gz

RUN tar -xvzf boost_1_54_0.tar.gz

WORKDIR /boost_1_54_0

RUN ./bootstrap.sh --prefix=/usr/local 
RUN ./b2; exit 0
RUN ./b2 install; exit 0

WORKDIR /

RUN git clone https://github.com/colemaring/unitree_legged_sdk.git unitree_legged_sdk

WORKDIR /unitree_legged_sdk

RUN mkdir build

WORKDIR build

RUN cmake -DPYTHON_BUILD=TRUE ..

RUN make
