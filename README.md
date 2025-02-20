# Projet : Solution OCR pour la gestion des quittances d'assurance

## Description
Ce projet utilise **PaddleOCR** pour extraire et traiter du texte en **français** et **arabe** à partir de quittances d'assurance. L'objectif est d'automatiser la reconnaissance et l'intégration des quittances dans un système de gestion.

## Technologies utilisées
- **Python 3.x**
- **PaddleOCR**
- **EasyOCR**
- **Tesseract OCR**
- **OCR.space API**
- **OpenCV**
- **Django (pour le backend)**
- **React.js (pour le frontend - optionnel)**

## Comparaison des solutions OCR utilisées
- **PaddleOCR** : Meilleure performance globale, mais nécessite une configuration correcte pour gérer plusieurs langues.
- **EasyOCR** : Performance moyenne, mais son point fort est de lire deux langues en même temps sans configuration complexe.
- **Tesseract OCR** : La performance la plus faible parmi les solutions testées.
- **OCR.space API** : Limité à **25 000 requêtes par mois**, ce qui pose problème lors de nombreux tests avec des quittances.

## Installation
### 1. Cloner le dépôt
```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_PROJET>
```

### 2. Installer les dépendances
Assurez-vous d'avoir **pip** installé, puis exécutez :
```bash
pip install -r requirements.txt
```

### 3. Installer PaddleOCR et PaddlePaddle
```bash
pip install paddlepaddle
pip install paddleocr
```

## Utilisation
### 1. Lancer l'extraction OCR
Exécutez le script suivant pour tester l'OCR sur une quittance :
```bash
python testPaddleOCR.py --image chemin/vers/image.jpg
```

### 2. Exemple de code OCR
```python
from paddleocr import PaddleOCR

# Initialisation de PaddleOCR pour le français et l'arabe
ocr = PaddleOCR(use_angle_cls=True, lang='fr|ar')

# Analyse d'une image
img_path = 'chemin/vers/image.jpg'
result = ocr.ocr(img_path, cls=True)

# Affichage des résultats
for line in result[0]:
    print(f"Texte : {line[1][0]} | Confiance : {line[1][1]}")
```

## Problèmes fréquents et solutions
- **Problème : PaddleOCR ne reconnaît pas plusieurs langues**  
  **Solution** : Utiliser `lang='fr|ar'` au lieu de `lang='fr,ar'`
  
- **Problème : Module introuvable**  
  **Solution** : Vérifier l'installation avec `pip list | grep paddle`

## Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une **issue** ou à soumettre une **pull request**.

## Auteur
- **[Ton Nom]**

## Licence
Ce projet est sous licence MIT.

