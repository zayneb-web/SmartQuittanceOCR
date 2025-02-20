import easyocr

# Lire le texte en français
reader_fr = easyocr.Reader(['fr'])
result_fr = reader_fr.readtext("photos/hP0006.jpg")
print("Texte en français :")
for text in result_fr:
    print(text[1])

# Lire le texte en arabe
reader_ar = easyocr.Reader(['ar', 'en'])  # L'arabe fonctionne avec l'anglais
result_ar = reader_ar.readtext("photos/hP0006.jpg")
print("Texte en arabe :")
for text in result_ar:
    print(text[1])
