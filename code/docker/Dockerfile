FROM sgtwilko/rpi-raspbian-opencv:latest
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Install python 3.8 and pip, but before install openssl 1.1.1
RUN apt-get update && apt-get upgrade
RUN apt-get install -y --no-install-recommends build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev tar wget vim
RUN cd /usr/src/ \
    && wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz \
    && tar -zxf openssl-1.1.1g.tar.gz \
    && cd openssl-1.1.1g \
    && ./config shared --prefix=/usr/local/ \
    && make \
    && make install \
    && mkdir lib 
RUN cp ./*.{so,so.1.0.0,a,pc} ./lib
RUN wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz \
    && tar -zxf Python-3.8.0.tgz
RUN cd Python-3.8.0 \
    && ./configure --with-openssl=/usr/src/openssl-1.1.1g --enable-optimizations \
    && make -j 4 \
    && make altinstall

# Create some useful symlinks
RUN cd /usr/local/bin \
    && ln -s idle3.8 idle \
    && ln -s pydoc3.8 pydoc \
    && ln -s python3.8 python \
    && ln -s python3.8-config python-config

# Copy scripts & set working directory
COPY app /intellicatflap/app/
WORKDIR /intellicatflap
RUN mkdir data

#RUN pip install --requirement /tmp/requirements.txt

# Run app
CMD ["app/detect_cat.py"]
