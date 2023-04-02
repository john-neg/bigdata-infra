#Create network
docker network create -d bridge bigdata-network
#Create hadoop base image
cd hadoop/base && docker build . -t hadoop-base && cd ../..
#Create spark base image
cd spark/base && docker build . -t spark-base && cd ../..
#Create jupyter base image
cd jupyter/base && docker build . -t jupyter-base && cd ../..
#Start all containers
docker-compose up