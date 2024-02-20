import io
import fitz
from PIL import Image
import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detec_face(images):
    faces = 0
    for image in images:
        image_array = np.asarray(image)
        if len(image_array.shape) == 2:
            image_array = cv2.cvtColor(image_array, cv2.COLOR_GRAY2BGR)
        detected_faces = face_cascade.detectMultiScale(image_array, 1.3, 6, minSize=(30, 30), maxSize=(300, 300))
        for (x, y, w, h) in detected_faces:
            rect_img = cv2.UMat(image_array)
            cv2.rectangle(rect_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            image_array = rect_img.get()
            faces += 1
    return faces

def extract_images_from_pdf(pdf_path, page_num):
    images = []
    pdf_document = fitz.open(pdf_path)
    
    page = pdf_document[page_num]
    image_list = page.get_images(full=True)
    for img_index, img_info in enumerate(image_list):
        xref = img_info[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image = Image.open(io.BytesIO(image_bytes))
        images.append(image)
    return images

def decode_qr_codes(images):
    qr_codes = []
    for image in images:
        width, height = image.size
        img = cv2.resize(np.array(image), (width*6, height*6))
        decoded_objects = pyzbar.decode(img)
        for obj in decoded_objects:
            try:
                qr_data = obj.data.decode('utf-8')
                qr_codes.append(qr_data)
            except:
                pass
    return qr_codes

def detect_ine(qr_code, num_page):
    if "ine" in qr_code:
        # print(qr_code)
        print("INE found in page ", num_page)
        return True
    return False

def detect_cfe(qr_code, num_page):
    if "cfe" in qr_code:
        # print(qr_code)
        print("CFE found in page ", num_page)
        return True
    return False

def detect_curp(qr_code, num_page):
    if "|" in qr_code:
        # Obtener la parte del CURP antes del primer "|"
        curp_part = qr_code.split("|")[0]
        # Verificar si la longitud de la parte del CURP es igual a la longitud de un CURP válido
        if len(curp_part) == 18:
            # print(qr_code.split("|")[0])
            print("CURP found in page ", num_page)
            return True
    return False

def detect_acta_nacimiento(qr_code, num_page):
    if "CURP" in qr_code:
        # print(qr_code)
        print("Acta de nacimiento found in page ", num_page)
        return True
    return False

def main(pdf_path):
    pdf_document = fitz.open(pdf_path)
    for i in range(len(pdf_document)):
        images = extract_images_from_pdf(pdf_path, i)
        qr_codes = decode_qr_codes(images)
        faces = detec_face(images)
        if qr_codes:
            for qr_code in qr_codes:
                if detect_ine(qr_code, i+1):
                    break
                elif detect_cfe(qr_code, i+1):
                    break
                elif detect_curp(qr_code, i+1):
                    break
                elif detect_acta_nacimiento(qr_code, i+1):
                    break
        elif faces >= 2:
            print("INE found in page ", i+1)
    
if __name__ == "__main__":
    inicio = time.time()
    pdf_path = "prueba_final.pdf"
    main(pdf_path)
    final = time.time()
    print("Tiempo de ejecución: ", final-inicio)
