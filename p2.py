#XABIJG REIBAX

import cv2

#Cargamos imagen
original_image = cv2.imread('image.png')

#Escala de grises
grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

#Gaussian blur para reducir ruido 17KERNEL
blurred_image = cv2.GaussianBlur(grayscale_image, (15,15), 0)

#Metodo Otsu para segmentacion
ret, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Busqueda de contornos para nucleos celulares
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Dibujo de los contornos
cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)

#Variable apra la media
total_size = 0

for idx, contour in enumerate(contours):
    #Dimensiones de las celulas 
    if(cv2.contourArea(contour)<10000):
        size = cv2.contourArea(contour)
        print(f'Nucleus {idx+1} size: {size} px^2')
        #total
        total_size += size
    
        

#Media
average_size = total_size / (len(contours)-1)
print(f'Average size of nuclei: {average_size} px^2')

#Mostramos resultados graficos
cv2.imshow('Segmented Nuclei', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
