import cv2 as cv #importation de la bibliotheque opencv as cv
img = cv.imread('photos/hP0006.jpg') #lecture de l'image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Maghrebia', img) #affichage de l'image dans une fenetre nommée Maghrebia 
cv.waitKey(0) #attente d'une touche pour fermer la fenetre
cv.destroyAllWindows() #fermer toutes les fenetres




