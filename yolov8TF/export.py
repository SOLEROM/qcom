import sys
from ultralytics import YOLO

def export(path):
    model = YOLO(path)
    model.export(format="tflite")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_model>")
        sys.exit(1)

    model_path = sys.argv[1]
    export(model_path)


