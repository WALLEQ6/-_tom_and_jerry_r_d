from ultralytics import YOLOv10
import os

os.environ["GIT_PYTHON_REFRESH"]="quiet"
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
if __name__ == '__main__':
    # Load a model
    # model = YOLO('yolov9c.yaml')  # build a new model from YAML
    # model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    model = YOLOv10(r'C:\Users\86152\yolov10\ultralytics\cfg\models\v10\yolov10s.yaml').load('yolov10s.pt')  # build from YAML and transfer weights

    # Train the model
    results = model.train(data=r'C:\Users\86152\yolov10\yolov3detecting\data.yaml', epochs=20, batch=20, imgsz=640)
