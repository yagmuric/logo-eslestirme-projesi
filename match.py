import cv2
import numpy as np
import os

# === KLASÖR YOLLARI ===
logos = "C:/Proje/data/logos"  # Veri tabanındaki logoların klasörü
query_path = "C:/Proje/data/query/logo.png"  # Aramak istediğin logo

# === Renk Histogramı Hesaplama ===
def renk_histogram(img):
    if img is None:
        return None
    img = cv2.resize(img, (200, 200))  # Tüm resimler aynı boyutta
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([img_hsv], [0, 1], None, [50, 60], [0, 180, 0, 256])
    cv2.normalize(hist, hist)
    return hist

# === Şekil (Kenar) Özellikleri ===
def sekil_ozellik(img):
    if img is None:
        return None
    img = cv2.resize(img, (200, 200))  # Tüm resimler aynı boyutta
    gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gri, (5, 5), 0)
    kenar = cv2.Canny(blur, 100, 200)
    return kenar

# === Benzerlik Hesaplama ===
def benzerlik(query_img, db_img):
    hist1 = renk_histogram(query_img)
    hist2 = renk_histogram(db_img)
    if hist1 is None or hist2 is None:
        return 0

    renk_score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

    edge1 = sekil_ozellik(query_img)
    edge2 = sekil_ozellik(db_img)
    if edge1 is None or edge2 is None:
        return 0

    sekil_score = np.sum(edge1 == edge2) / edge1.size
    toplam_score = (renk_score + sekil_score) / 2
    return toplam_score

# === ANA PROGRAM ===
if __name__ == "__main__":
    # Sorgu logosunu oku
    query_img = cv2.imread(query_path)
    if query_img is None:
        print(f"HATA: {query_path} dosyası okunamadı! Yolunu kontrol et.")
        exit()

    results = []

    for file in os.listdir(logos):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(logos, file)
            db_img = cv2.imread(img_path)
            if db_img is None:
                print(f"Uyarı: {file} okunamadı, geçiliyor.")
                continue

            score = benzerlik(query_img, db_img)
            results.append((file, score))

    if not results:
        print("Hiç eşleşme bulunamadı.")
        exit()

    results.sort(key=lambda x: x[1], reverse=True)

    print("\n--- EŞLEŞME SONUÇLARI ---")
    for file, score in results:
        print(f"{file} => Benzerlik Puanı: {score:.4f}")

    # En benzer resmi göster
    best_match_path = os.path.join(logos, results[0][0])
    best_match = cv2.imread(best_match_path)

    cv2.imshow("Query Logo", query_img)
    cv2.imshow("Best Match", best_match)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
