import cv2
import numpy as np

def aplicar_transformada_hough_circulos(imagen, umbral_votos, min_distancia, min_radio, max_radio):
    # Se realiza copia de la imagen original para realiar las modificaciones
    copia = imagen.copy()  

    # Se convierte la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Se aplicar la transformada de Hough para detectar círculos
    circulos = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT, 1, min_distancia,
                                param1=umbral_votos, param2=min_radio, minRadius=min_radio, maxRadius=max_radio)

    # Se dibujab los círculos detectados en la copia de la imagen original
    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype("int")
        for (x, y, r) in circulos:
            cv2.circle(copia, (x, y), r, (0, 0, 255), 2)

    return copia

# Se carga la imagen para analizar
imagen = cv2.imread('imagen2.jpg')

# Se definene los parámetros de la transformada de Hough para círculos
#umbral_votos = 30
#min_distancia = 50
#min_radio = 10
#max_radio = 100
#umbral_votos = 25
#min_distancia = 40
#min_radio = 38
#max_radio = 48
umbral_votos = 28
min_distancia = 38
min_radio = 40
max_radio = 50

# Se aplica la transformada de Hough a la imagen
resultado = aplicar_transformada_hough_circulos(imagen, umbral_votos, min_distancia, min_radio, max_radio)

# Se muestra la imagen original sin círculos
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)

# Se muestra la imagen resultante con los círculos detectados
cv2.imshow('Transformada de Hough - Círculos', resultado)
cv2.waitKey(0)

cv2.destroyAllWindows()