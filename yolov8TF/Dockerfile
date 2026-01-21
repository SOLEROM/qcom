FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    unzip \
    python3 \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libusb-1.0-0 \
    cmake build-essential git python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# RUN pip3 install ultralytics tensorflow onnx "onnx2tf>1.17.5,<=1.22.3" onnxruntime onnxslim "onnx_graphsurgeon>=0.3.26" "sng4onnx>=1.0.1" tf_keras tflite_support
RUN python3 -m pip install --only-binary=:all: ultralytics tensorflow onnx "onnx2tf>1.17.5,<=1.22.3" onnxruntime onnxslim "onnx_graphsurgeon>=0.3.26" "sng4onnx>=1.0.1" tf_keras tflite_support
