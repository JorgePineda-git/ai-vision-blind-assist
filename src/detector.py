import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

id_classes = [0, 2, 42, 56, 57, 60, 67, 72, 73, 79]
min_conf = 0.45

def procesar_frame(frame):
    results = model(frame, verbose=False, conf=min_conf, classes=id_classes)
    det_boxes = results[0].boxes

    for box in det_boxes:
        id_class = int(box.cls[0])
        conf = float(box.conf[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        name_class = model.names[id_class]
        tag = f"{name_class} ({conf:.2f})"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"{tag}", (x1+10, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (255, 0, 0), 2)
    
    return frame
