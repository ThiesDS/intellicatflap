# Not an official base image, but it runs tf2 on arm architectures
FROM francoisgervais/tensorflow:2.1.0-cp35
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install python requirements
COPY requirements.txt .
RUN pip install --requirement requirements.txt

# Clone repo and install tf object detection api
RUN mkdir tensorflow \
    && cd tensorflow \
    && git clone --depth 1 https://github.com/tensorflow/models 
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y protobuf-compiler
RUN cd tensorflow/models/research/ \
    && protoc object_detection/protos/*.proto --python_out=. \
    && cp object_detection/packages/tf2/setup.py . \
    && python -m pip install .

# Download pretrained model
RUN mkdir pretrained_models && cd pretrained_models \
    && wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz \
    && tar -xf ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz

# Create app folder
RUN mkdir /app/
WORKDIR /app/

# Copy app
COPY app .

# Run app
CMD ["python","main.py"]