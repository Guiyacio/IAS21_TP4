import cv2
import numpy as np

def aplicar_transformada_hough(imagen, umbral_votos):
    # Se convierte la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Se aplica la detección de bordes utilizando el operador de Canny
    bordes = cv2.Canny(gris, 50, 150)

    # Se aplica la transformada de Hough para detectar líneas
    lineas = cv2.HoughLines(bordes, 1, np.pi / 180, umbral_votos)

    # Se crea una copia de la imagen original
    imagen_copia = imagen.copy()

    # Se dibujan las líneas detectadas en la copia de la imagen original
    if lineas is not None:
        for linea in lineas:
            rho, theta = linea[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(imagen_copia, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return imagen_copia

# Se carga la imagen para analizar
imagen = cv2.imread('imagen.jpg')

# Se definen los parámetros de la transformada de Hough
resolucion_distancia = 1
resolucion_angulo = np.pi / 180
#umbral_votos = 150
umbral_votos = 100

# Se aplica la transformada de Hough a la imagen
resultado = aplicar_transformada_hough(imagen, umbral_votos)

# Se muestran la imagen original y el resultado
cv2.imshow('Original', imagen)
cv2.imshow('Transformada de Hough', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()