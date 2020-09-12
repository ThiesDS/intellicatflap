FROM sgtwilko/rpi-raspbian-opencv:latest
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Install python 3.8 and pip
RUN apt-get update && apt-get upgrade
RUN apt-get install -y --no-install-recommends build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz \
    && tar -zxf Python-3.8.0.tgz
RUN cd Python-3.8.0 \
    && ./configure --enable-optimizations \
    && make -j 4 \
    && make altinstall


# Copy scripts & set working directory
COPY app /intellicatflap/app/
COPY app /intellicatflap/app/
WORKDIR /intellicatflap
RUN mkdir data

#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    python3.8 \
#    python3-pip \
#RUN apt-get clean \
#    rm -rf /var/lib/apt/lists/*

RUN pip --version
RUN pip3 --version 


# Install dependencies
#RUN pip3 install --upgrade pip3 && \
#    pip3 install --no-cache-dir pathlib2
#RUN pip3 install --no-cache-dir opencv-python

#COPY requirements.txt /tmp/
#RUN pip install --requirement /tmp/requirements.txt

# Run app
CMD ["app/detect_cat.py"]
