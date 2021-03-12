FROM python:3.9.0-buster
LABEL maintainer "Sven Thies <sven_thies@web.de>"

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