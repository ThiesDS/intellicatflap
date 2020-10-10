FROM sgtwilko/rpi-raspbian-opencv:jessie-4.1.1
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Create app folder
RUN mkdir /app/
WORKDIR /app/

# Install python requirements
COPY requirements.txt .
RUN pip install --requirement requirements.txt

# Copy app
COPY app .

# Create data dir to store images
RUN mkdir data

# Add non-root user 
#RUN useradd -ms /bin/bash duser
#USER duser

# Run app
CMD ["python3","record_cat.py"]
