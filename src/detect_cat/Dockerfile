# Not an official base image, but it runs tf2 on arm architectures
FROM francoisgervais/tensorflow:2.1.0-cp35
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Install python>3.6 (required for object detection api)
RUN apt-get -qq update && apt-get -qq upgrade \
    && apt-get install -y make build-essential libssl-dev zlib1g-dev
RUN apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
RUN apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev
RUN wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz \
    && tar xvf Python-3.6.4.tgz \
    && cd Python-3.6.4 \
    && ./configure --enable-optimizations \
    && make -j8 \
    && make altinstall

RUN python3.6 --version

# Install python and  requirements
COPY requirements.txt .
RUN pip3 install --requirement requirements.txt

# Clone repo and install tf object detection api
RUN apt-get update -y && apt-get upgrade -y \ 
    && apt-get install -y git \
    && apt-get install -y protobuf-compiler
RUN mkdir tensorflow \
    && cd tensorflow \
    && git clone --depth 1 https://github.com/tensorflow/models 
RUN cd tensorflow/models/research/ \
    && protoc object_detection/protos/*.proto --python_out=. \
    && cp object_detection/packages/tf2/setup.py . \
    && python3 -m pip install .

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
