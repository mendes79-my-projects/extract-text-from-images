# opencv - pip install opencv-python -> import cv2
# pytesseract - C:\Program Files\Tesseract-OCR

import cv2
import pytesseract

# carregar a imagem com opencv / load the image with opencv
# informe o diretório e nome da imagem / Enter the directory and name of the image file
img = cv2.imread("Images\example03.png")

# indicar onde fica o executável do pytesseract / path to pytesseract executable file
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/Tesseract.exe"

# configuração para o modo de reconhecimento do texto, para ajudar no reconhecimento
# config = r'--oem 3 --psm 6'

# reconhecendo o nome ou texto escrito na imagem / to extract text from image
nome = pytesseract.image_to_string(img)

print("")
print(nome)