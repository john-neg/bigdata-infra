FROM python:3.10

ARG SPARK_VERSION="3.3.2"
ARG JUPYTERLAB_VERSION="3.6.2"
#ARG SCIKIT_LEARN_VERSION="1.2.0"

ENV SHARED_WORKSPACE /opt/workspace
RUN mkdir -p $SHARED_WORKSPACE/data
RUN mkdir -p /usr/share/man/man1

RUN apt update && apt upgrade -y
RUN apt install openjdk-11-jdk -y
RUN pip install --upgrade pip

VOLUME $SHARED_WORKSPACE
CMD ["bash"]

COPY workspace/ $SHARED_WORKSPACE

RUN pip3 install -U wget pyspark==${SPARK_VERSION} jupyterlab==${JUPYTERLAB_VERSION} \
                    pandas numpy scipy seaborn matplotlib requests \
                    joblibspark scikit-learn

EXPOSE 8888

WORKDIR $SHARED_WORKSPACE

ENV PYSPARK_PYTHON=/usr/bin/python3.10
ENV PYSPARK_DRIVER_PYTHON=3.10

CMD ["jupyter" , "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=", "--NotebookApp.password=''"]