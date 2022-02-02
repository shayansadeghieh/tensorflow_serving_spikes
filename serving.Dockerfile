FROM ml6team/tf-serving-tfdf:latest

ARG MODELID=

ENV MODEL_NAME=${MODELID}

COPY weights /models/${MODELID}/0

EXPOSE 8501
