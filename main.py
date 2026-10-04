import cv2
import time
from src.detector import procesar_frame

vid = 0
cap = cv2.VideoCapture(vid)
if not cap.isOpened():
    print("No se pudo acceder a webcam")
    exit()
print("Camara abierta correctamente")


alpha = 0.02
fps_smooth = 0
time_inicio = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer fotograma de la cámara")
        break

    frame = procesar_frame(frame)

    time_actual = time.time()
    delta_time = time_actual - time_inicio
    time_inicio = time_actual

    fps_instant = 1 / delta_time if delta_time > 0 else 0 

    if fps_smooth == 0:
        fps_smooth = fps_instant
    
    fps_smooth = ((1-alpha)*fps_smooth) + (alpha*fps_instant)

    cv2.putText(frame, f"FPS: {fps_smooth:.0f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Captura imagen", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()