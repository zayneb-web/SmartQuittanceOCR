from paddleocr import PaddleOCR

# Initialiser PaddleOCR avec français et arabe
ocr = PaddleOCR(use_angle_cls=True, lang='fr|ar')

# Spécifier l'image à analyser
img_path = 'photos/hP0006.jpg'              

# Effectuer la reconnaissance de texte
result = ocr.ocr(img_path, cls=True)

# Afficher les résultats
for line in result[0]:
    print(f"Texte : {line[1][0]} | Confiance : {line[0]}")
