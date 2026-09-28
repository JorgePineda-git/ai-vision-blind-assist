import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo acceder a webcam")
    exit()

print("Camara abierta con éxito")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer fotograma de la cámara")
        break

    cv2.imshow("Captura imagen", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()