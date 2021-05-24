FROM python:3.9.0-slim-buster

LABEL maintainer "Sven Thies <sven_thies@web.de>"

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
&&  pip install -r requirements.txt \
&&  mkdir /app \
&&  mkdir /app/credentials \
&&  rm -rf /root/.cache \
&&  apt-get -qqy autoremove --purge \
&&  useradd -ms /bin/bash gcssync

USER gcssync

WORKDIR app/

COPY app .

CMD ["python","main.py"]
