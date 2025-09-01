import os
from PIL import Image

# Logoların bulunduğu klasör 
klasor = "C:\\data\\logos"

# Klasördeki tüm dosyaları dolaş
for dosya in os.listdir(klasor):
    if dosya.lower().endswith((".jpg", ".png", ".jpeg")):
        yol = os.path.join(klasor, dosya)
        try:
            with Image.open(yol) as img:
                print(f"{dosya}: {img.size}")
        except Exception as e:
            print(f"{dosya} okunamadı: {e}")
