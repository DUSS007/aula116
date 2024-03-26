import cv2

#leia a image
img = cv2.imread("buttlefly.jpg")

#exiba a imagem colorida
cv2.imshow("Image de exibicao",img)

#converta a imagem colorida para escala de cinza
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#exiba a imagem em escala de cinze
cv2.imshow("Escala de Cinza",gray_img)

#print(gray_img)
cv2.waikey(0)