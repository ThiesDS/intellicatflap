FROM tensorflow/serving:latest
LABEL maintainer "Sven Thies <sven_thies@web.de>"

RUN apt-get update -y && apt-get upgrade -y 
RUN apt-get install wget -y
RUN wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz \
    && tar -xvf ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz \
    && rm ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz \
    && mkdir /models/mobilenet && mkdir models/mobilenet/1 \
    && cp -r ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8/saved_model /models/mobilenet/1/