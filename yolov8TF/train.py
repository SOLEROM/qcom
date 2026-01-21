import yaml
from ultralytics import YOLO
import torch

def load_training_params(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def train(params):
    model = YOLO('yolov8n.pt')
    results = model.train(
        data=params['data'],
        imgsz=params['imgsz'],
        epochs=params['epochs'],
        batch=params['batch'],
        name=params['name'],
        workers=params['workers'],
        plots=params['plots']
    )

def check_gpu():
    if torch.cuda.is_available():
        print(f"PyTorch detected {torch.cuda.device_count()} GPU(s):")
        for i in range(torch.cuda.device_count()):
            print(f" - GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("PyTorch did not detect any GPUs.")

if __name__ == '__main__':
    try:
        check_gpu()
    except Exception as e:
        print(f"PyTorch check failed with error: {e}")
    
    print("Training started")
    params = load_training_params('model_train.yaml')
    train(params)


