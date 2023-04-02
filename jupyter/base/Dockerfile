FROM python:3.10

ARG SPARK_VERSION="3.3.2"
ARG JUPYTERLAB_VERSION="3.6.3"

RUN mkdir -p /usr/share/man/man1

RUN apt update && apt upgrade -y
RUN apt install openjdk-11-jdk -y
RUN pip install --upgrade pip

CMD ["bash"]

RUN pip3 install -U wget pyspark==${SPARK_VERSION} jupyterlab==${JUPYTERLAB_VERSION} \
                    pandas numpy scipy seaborn matplotlib requests \
                    joblibspark scikit-learn

ENV PYSPARK_PYTHON=/usr/bin/python3.10
ENV PYSPARK_DRIVER_PYTHON=3.10