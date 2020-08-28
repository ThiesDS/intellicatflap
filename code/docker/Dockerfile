FROM sgtwilko/rpi-raspbian-opencv:latest
LABEL maintainer "Sven Thies <sven_thies@web.de>"

# Copy scripts & set working directory
COPY app /intellicatflap/app/
WORKDIR /intellicatflap
RUN mkdir data

# Install dependencies


# Run app
CMD ["app/detect_cat.py"]