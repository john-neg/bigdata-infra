FROM openjdk:11-jre-slim

ARG DEBIAN_FRONTEND=noninteractive
ARG SCALA_VERSION="2.12.17"
ARG SPARK_VERSION="3.3.2"
ARG HADOOP_VERSION="3"

ENV SHARED_WORKSPACE /opt/workspace

RUN mkdir -p $SHARED_WORKSPACE/data
RUN mkdir -p /usr/share/man/man1
RUN apt-get update -y
RUN apt-get install -y curl python3 r-base
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN curl https://downloads.lightbend.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb -k -o scala.deb
RUN apt install -y ./scala.deb
RUN rm -rf scala.deb /var/lib/apt/lists/*

ENV SCALA_HOME /usr/bin/scala
ENV PATH=${PATH}:${SCALA_HOME}/bin
ENV SPARK_HOME /usr/bin/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}

VOLUME $SHARED_WORKSPACE
CMD ["bash"]

RUN curl https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /usr/bin/ && \
    echo "alias pyspark=$SPARK_HOME/bin/pyspark" >> ~/.bashrc && \
    echo "alias spark-shell=$SPARK_HOME/bin/spark-shell" >> ~/.bashrc && \
    mkdir $SPARK_HOME/logs && \
    rm spark.tgz

ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

WORKDIR $SPARK_HOME