# 

## deps

```
nvidia-smi
```

## install

* based on local Dockerfile (40GB)
```
docker build -t yolov8-train:latest .
```

## run

```
docker run --gpus all -it -v .:/app/ yolov8-train:latest
docker run --gpus all -it --shm-size=16g --cpus="4" -v .:/app/ yolov8-train:latest /bin/bash
```

## in docker:

train and export to tflite:

```
> python3 train.py
> python3 export.py best.pt
```

result with:
```
best_saved_model/
    best_float16.tflite
    best_float32.tflite
```

