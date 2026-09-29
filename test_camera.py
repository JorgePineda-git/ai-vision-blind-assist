import cv2
import time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo acceder a webcam")
    exit()
print("Camara abierta correctamente")

time_inicio = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer fotograma de la cámara")
        break

    time_actual = time.time()
    delta_time = time_actual - time_inicio
    time_inicio = time_actual

    fps = 1 / delta_time if delta_time > 0 else 0 

    cv2.putText(frame, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Captura imagen", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()