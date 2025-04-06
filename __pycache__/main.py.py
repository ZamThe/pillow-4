import cv2

def escanear_con_webcam(output_path="escaneo.jpg"):
    cap = cv2.VideoCapture(0)  # Usa 0 si el escáner aparece como cámara

    if not cap.isOpened():
        print("❌ No se pudo abrir la cámara. Verifica la conexión del escáner.")
        return

    print("📸 Presiona 'ESPACIO' para capturar la imagen y 'ESC' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error al obtener imagen.")

        cv2.imshow("Escáner / Cámara", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 32:  # Tecla ESPACIO para capturar
            cv2.imwrite(output_path, frame)
            print(f"✅ Imagen guardada como {output_path}")
            break
        elif key == 27:  # Tecla ESC para salir
            break

    cap.release()
    cv2.destroyAllWindows()

# Llamar a la función para escanear
escanear_con_webcam()
