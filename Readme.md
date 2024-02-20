# Documentación
## Descripción general

### Este código elaborado en Python se encarga de procesar archivos PDF de agencias automotrices que continen el expediente del cliente que son documentos impresos escaneados, para posteriormente identificar en que páginas se encuentran los documentos de identificación oficial en México tales como la INE, el comprobante de luz de CFE, la CURP y el acta de nacimiento a través del análisis de los códigos QR presentes en los documentos así como la identificación de rostros en el caso de la INE.

### El código incluye varias funciones que cumplen con funciones específicas. Primero, extrae las imágenes de cada página del PDF y las almacena en una lista. Luego, detecta códigos QR en las imágenes y los decodifica. Finalmente, verifica si los códigos QR corresponden a ciertos tipos de documentos de identificación oficial, como una credencial para votar, una factura de electricidad, etc.

## Requisitos funcionales

- ### RF-1: El programa debe mostrar al usuario en que pagina del pdf se encuentra la identificación oficial INE
- ### RF-2: El programa debe mostrar al usuario en que pagina del pdf se encuentra la CURP
- ### RF-3: El programa debe mostrar al usuario en que pagina del pdf se encuentra el recibo de luz de CFE
- ### RF-4: El programa debe mostrar al usuario en que pagina del pdf se encuentra el acta de nacimiento

## Requisitos no funcionales

- ### RNF-1: El programa debe ser capaz de procesar un PDF de 22 hojas en menos 80 segundos
- ### RNF-2: El programa debe ser capaz de procesar archivos PDF con documentos escaneados diferentes estados
- ### RNF-3: El programa no debe arrojar falsos positivos
- ### RNF-4: El programa debe ser capaz de ajustarse sus parametros para mejores resultados

## Restricciones de recursos:

- ### RR-1: El sistema debe ser capaz de manejar archivos PDF donde los documentos a buscar tengan un código QR.
- ### RR-2: El sistema debe ser capaz de manejar archivos PDF donde el grado de deterioro no afecte significativamente los códigos QR.

## Restricciones de hardware:

- ### RH-1: El sistema debe ser compatible con el sistema operativo Windows.

## Funciones
- ### detec_face(images): Esta función detecta la presencia de rostros en una lista de imágenes. Utiliza un clasificador en cascada de Haar para detectar rostros en imágenes en escala de grises. Devuelve el número total de rostros detectados en todas las imágenes.

- ### extract_images_from_pdf(pdf_path, page_num): Esta función extrae las imágenes de una página específica de un archivo PDF. Utiliza la biblioteca fitz para abrir y leer el PDF, y la función get_images para obtener una lista de las imágenes de la página. Luego, utiliza la función extract_image para extraer cada imagen de la página y la convierte en un objeto de imagen de PIL. Devuelve una lista de objetos de imagen.

- ### decode_qr_codes(images): Esta función decodifica los códigos QR en una lista de imágenes. Utiliza la biblioteca pyzbar para decodificar los códigos QR en cada imagen. Devuelve una lista de datos decodificados.

- ### detect_ine(qr_code, num_page): Esta función verifica si un código QR corresponde a una credencial para votar. Valida que en los metadatos del código QR se encuentre la palabra "INE" para determinar si es una credencial para votar. Devuelve un valor booleano que indica si el código QR corresponde a una credencial para votar.

- ### detect_cfe(qr_code, num_page): Esta función verifica si un código QR corresponde a una factura de electricidad. Valida que en los metadatos del código QR se encuentre la palabra "CFE" para determinar si es una factura de electricidad. Devuelve un valor booleano que indica si el código QR corresponde a una factura de electricidad.

- ### detect_curp(qr_code, num_page): Esta función verifica si un código QR corresponde a una Clave Única de Registro de Población (CURP). Valida que en los metadatos del código QR tenga la estructura que corresponde a una CURP para determinar si es una CURP válida. Devuelve un valor booleano que indica si el código QR corresponde a una CURP válida.

- ### detect_acta_nacimiento(qr_code, num_page): Esta función verifica si un código QR corresponde a un acta de nacimiento. Valida que en los metadatos del código QR se encuentre la palabra "CURP" para determinar si es un acta de nacimiento. Devuelve un valor booleano que indica si el código QR corresponde a un acta de nacimiento.

- ### main(pdf_path): Esta función principal recibe la ruta de un archivo PDF y realiza todo el proceso de detección. Utiliza las funciones anteriores para extraer imágenes, decodificar códigos QR y verificar si los códigos QR corresponden a documentos de identificación oficial. Imprime mensajes en la consola para indicar en que página se han encontrado documentos de identificación oficial y cuales son.

## Decisiones de diseño

### El código utiliza un enfoque modular, lo que permite que cada función realice una tarea específica. Esto facilita la comprensión, el mantenimiento y la evolución del código. Además, está desarrollado en Python lo que facilita el uso de bibliotecas de terceros para realizar tareas específicas, como la detección de rostros, la extracción de imágenes de PDF y la decodificación de códigos QR, lo que permite reutilizar código existente y aprovechar las capacidades de estas bibliotecas.

### El código utiliza una estrategia de detección basada en la presencia de ciertas cadenas de texto en los códigos QR. Esto permite detectar documentos de identificación oficial sin necesidad de analizar el contenido completo de los códigos QR, lo cual permite que haya una alta confiabilidad debido a que en el contexto del problema no podrían haber falsos positivos.

### El código utiliza la biblioteca OpenCV para detectar rostros en imágenes. Esto permite detectar rostros en imágenes en escala de grises y en imágenes en color. Además, utiliza un clasificador en cascada de Haar, que es un enfoque eficiente, preciso y confiable para la detección de rostros.

### El código utiliza la biblioteca PyMuPDF para interactuar con archivos PDF. Esto permite abrir y leer archivos PDF, extraer imágenes de archivos PDF y realizar otras operaciones relacionadas con PDF. Sin embargo, esta biblioteca no es compatible con todas las características de PDF, por lo que puede haber limitaciones en la manipulación de ciertos archivos PDF.

### El código utiliza la biblioteca PIL para trabajar con imágenes. Esto permite abrir, manipular y guardar imágenes en diferentes formatos. Sin embargo, esta biblioteca no es compatible con todas las características de imágenes, por lo que puede haber limitaciones en la manipulación de ciertas imágenes.