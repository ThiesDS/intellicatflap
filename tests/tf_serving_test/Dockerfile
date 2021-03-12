FROM python:3.9.0-buster
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# install open ssh and copy public key
RUN apt-get install -y git
RUN mkdir -m 700 /root/.ssh; \
    touch -m 600 /root/.ssh/known_hosts; \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Clone intellicatflap-analytics repo for testing utils
RUN --mount=type=ssh git clone --depth 1 git@github.com:ThiesDS/intellicatflap_analytics.git

# Upgrade pip & install python requirements
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install --requirement requirements.txt

# Create app folder & copy app
RUN mkdir /app/
WORKDIR /app/
COPY app .

# Add non-root user
RUN useradd -ms /bin/bash duser
USER duser

# Run app
CMD ["python","main.py"]