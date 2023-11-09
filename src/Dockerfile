# Use an official Python runtime as a parent image
FROM python:3.8

# Set working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    curl \
    autoconf \
    automake \
    libtool \
    pkg-config \
    build-essential \
    libsnappy-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the libpostal directory contents into the container at /libpostal
COPY libpostal /libpostal

# Add this line to adjust file permissions
RUN chmod +x /libpostal/bootstrap.sh

# Build and install libpostal
RUN cd /libpostal \
    && ./bootstrap.sh \
    && ./configure --datadir=/libpostal_data \
    && make -j4 \
    && make install \
    && ldconfig \
    && cd /app \
    && rm -rf /libpostal

# Install necessary python packages
RUN pip install --no-cache-dir flask gunicorn pybind11 postal

# Copy the app directory contents into the container at /app
COPY app /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the application
CMD ["gunicorn", "-b", ":8080", "app:app"]
