import cv2 as cv  # importation de la bibliothèque OpenCV

img = cv.imread('photos/hP0006.jpg')  # lecture de l'image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # conversion de l'image en niveaux de gris

# Fonction pour redimensionner l'image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # largeur de l'image
    height = int(frame.shape[0] * scale)  # hauteur de l'image
    dimensions = (width, height)  # dimensions de l'image
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # redimensionnement de l'image

# Redimensionner l'image en niveaux de gris
rescaled_gray = rescaleFrame(gray)

# Affichage de l'image en niveaux de gris et redimensionnée
cv.imshow('Maghrebia', rescaled_gray)

cv.waitKey(0)  # Attente d'une touche pour fermer la fenêtre
cv.destroyAllWindows()  # Ferme toutes les fenêtres
