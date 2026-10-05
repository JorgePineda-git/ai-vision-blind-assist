from ultralytics import YOLO
from src.detector import id_classes, min_conf

def evaluar_modelo():
    
    model = YOLO("yolov8n.pt")

    metrics = model.val(data="coco.yaml", split="val", classes=id_classes, conf=min_conf, verbose=True)
    
    precision_mean = metrics.box.mp
    recall_mean = metrics.box.mr
    map50 = metrics.box.map50
    map50_95 = metrics.box.map
    
    print("\n" + "="*55)
    print("      RESULTADOS DE EVALUACIÓN (TUS CLASES DEL PROYECTO)")
    print("="*55)

    print(f"Clases evaluadas:")
    for id in id_classes:
        print(f" - ID {id}: {model.names[id]}")
    print(f"Umbral de confianza: {min_conf}\n")

    print(f"  Precision Promedio (P) : {precision_mean:.4f} ({precision_mean * 100:.2f}%)")
    print(f"  Recall Promedio (R)    : {recall_mean:.4f} ({recall_mean * 100:.2f}%)")
    print(f"  mAP @ 0.50             : {map50:.4f} ({map50 * 100:.2f}%)")
    print(f"  mAP @ 0.50:0.95        : {map50_95:.4f} ({map50_95 * 100:.2f}%)")

if __name__ == "__main__":
    evaluar_modelo()