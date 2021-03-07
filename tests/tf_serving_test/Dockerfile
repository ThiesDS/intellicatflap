FROM python:3.9.0-buster
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Clone intellicatflap-analytics repo for testing utils
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y git
RUN git clone --depth 1 git@github.com:ThiesDS/intellicatflap_analytics.git

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