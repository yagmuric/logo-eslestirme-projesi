# Logo Eşleştirme Projesi

Bu proje, Türk Patent ve Marka Kurumu'ndan alınan logoları kullanarak **renk ve şekil özelliklerine göre benzerlik analizi** yapan bir sistemdir.  
Python ve OpenCV kütüphanesi ile geliştirilmiştir.

## 🚀 Özellikler
- Logoları otomatik olarak indirir ve standart dosya isimleriyle saklar
- Renk analizi için **K-Means algoritması**
- Şekil analizi için **Canny edge detection** ve kontur analizi
- Histogram tabanlı benzerlik puanı hesaplama
- Kullanıcıdan alınan logoyu veri tabanındaki logolarla karşılaştırma

## 🛠 Kullanılan Teknolojiler
- **Python 3.12**
- **OpenCV**
- **Pillow**
- **Requests**

## 📂 Proje Yapısı
/staj-proje
|-- kontrol.py # Logo boyut kontrolü
|-- dosya.py # Şekil ve renk analizi
|-- match.py # Logo eşleştirme algoritması
|-- data/logos/ # Logo görselleri

## 🔧 Kurulum
```bash
pip install opencv-python pillow requests
## çalıştırma
python match.py


