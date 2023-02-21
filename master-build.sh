#Create network
docker network create -d bridge bigdata-network
#Create hadoop base image
cd hadoop/base && docker build . -t hadoop-base && cd ../..
#Start all containers
docker-compose up