FROM openjdk:11-jre-slim

ARG DEBIAN_FRONTEND=noninteractive

ENV HADOOP_VERSION=3.3.4
ENV HADOOP_URL=https://dist.apache.org/repos/dist/release/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz \
    HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION \
    HADOOP_CONF_DIR=/etc/hadoop \
    MULTIHOMED_NETWORK=1 \
    USER=root
ENV PATH=$HADOOP_HOME/bin/:$PATH

RUN apt-get update  \
    && apt-get install -y apt-utils curl gnupg netcat procps  \
    && rm -rf /var/lib/apt/lists/*

RUN curl -O https://dist.apache.org/repos/dist/release/hadoop/common/KEYS

RUN gpg --import KEYS

RUN set -x \
    && curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && curl -fSL "$HADOOP_URL.asc" -o /tmp/hadoop.tar.gz.asc \
    && gpg --verify /tmp/hadoop.tar.gz.asc \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz*

RUN ln -s /opt/hadoop-$HADOOP_VERSION/etc/hadoop /etc/hadoop \
    && mkdir /opt/hadoop-$HADOOP_VERSION/logs \
    && mkdir /hadoop-data

ADD entrypoint.sh /entrypoint.sh

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
