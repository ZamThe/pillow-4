import cv2
import pytesseract
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

def extraer_texto(imagen_path):
    img = cv2.imread(imagen_path)

    if img is None:
        print(f"❌ Error: No se pudo cargar la imagen '{imagen_path}'. Verifica la ruta.")
        return None

   
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  
    _, img_bin = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

   
    try:
        texto = pytesseract.image_to_string(img_bin, lang='eng')

        print("\n📜 Texto extraído:")
        print("=" * 50)
        print(texto)
        print("=" * 50)
    except Exception as e:
        print("❌ Error al extraer texto:", e)

# Ruta de la imagen
imagen_path = r"C:\Users\zam\Desktop\Pillow\documento.JPG"


extraer_texto(imagen_path)
