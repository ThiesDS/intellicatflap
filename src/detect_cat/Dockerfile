FROM python:3.9.0-slim-buster

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
&&  pip install -r requirements.txt \
&&  mkdir -p /app \
             /app/data \
             /app/uploads \
&&  rm -rf /root/.cache \
&&  apt-get -qqy autoremove --purge \
&&  useradd -ms /bin/bash cdetector

USER cdetector

WORKDIR app/

COPY app .

CMD ["python","main.py"]
