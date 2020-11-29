FROM raspbian/stretch:latest
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Create app folder
RUN mkdir /app/
WORKDIR /app/

# Install python requirements
COPY requirements.txt .
RUN pip install --requirement requirements.txt

# Copy app
COPY app .

# Add non-root user and give access to webcam
RUN useradd -ms /bin/bash duser
USER duser

# Run app
CMD ["python","push_images_to_gcs.py"]
