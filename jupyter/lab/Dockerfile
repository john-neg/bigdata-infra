FROM jupyter-base

EXPOSE 8888

ENV SHARED_WORKSPACE /opt/workspace
RUN mkdir -p $SHARED_WORKSPACE/data

VOLUME $SHARED_WORKSPACE

COPY workspace/ $SHARED_WORKSPACE

WORKDIR $SHARED_WORKSPACE

CMD ["jupyter" , "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=", "--NotebookApp.password="]