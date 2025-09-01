import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Logo dosyasını oku
image = cv2.imread("C:/data/logos/logo_002.jpg")
if image is None:
    raise FileNotFoundError("Logo dosyası bulunamadı, yolunu kontrol et!")

# BGR -> RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ---- RENK ANALİZİ ----
resized = cv2.resize(image_rgb, (150, 150))
pixels = resized.reshape((-1, 3))

kmeans = KMeans(n_clusters=3, random_state=42).fit(pixels)
colors = kmeans.cluster_centers_.astype(int)

print("Baskın Renkler (RGB):", colors)

# ---- ŞEKİL ANALİZİ ----
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_img = image_rgb.copy()
cv2.drawContours(contour_img, contours, -1, (255, 0, 0), 2)

# Görselleştirme
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Orijinal Logo")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(contour_img)
plt.title("Kontur Analizi")
plt.axis("off")
plt.show()

# Örnek özellikler
for c in contours:
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print("Alan:", area, "Çevre:", perimeter)
