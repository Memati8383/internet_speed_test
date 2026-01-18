# 🚀 Aura SpeedTest Pro

Aura SpeedTest Pro, Python ve CustomTkinter kullanılarak geliştirilmiş, modern ve minimalist bir arayüze sahip internet hız testi uygulamasıdır. Kullanıcıların indirme (download), yükleme (upload) hızlarını ve ping sürelerini en şık şekilde ölçmelerini sağlar.

## ✨ Özellikler

- **Modern Arayüz:** CustomTkinter ile oluşturulmuş, Dark Mode temalı premium tasarım.
- **Gerçek Zamanlı Animasyonlar:** Test sırasında değişen renkler ve akıcı sayaç animasyonları.
- **Hassas Ölçüm:** `speedtest-cli` altyapısı ile güvenilir sonuçlar.
- **Kullanıcı Dostu:** Tek tıkla test başlatma ve net görsel geri bildirim.
- **Hafif ve Hızlı:** Minimum sistem kaynağı kullanımı.

## 🛠️ Kurulum (Geliştiriciler İçin)

Projeyi yerel makinenizde çalıştırmak için:

1.  **Depoyu Klonlayın:**

    ```bash
    git clone https://github.com/Memati8383/internet_speed_test.git
    cd internet_speed_test
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**

    ```bash
    pip install customtkinter speedtest-cli pillow
    ```

3.  **Uygulamayı Çalıştırın:**
    ```bash
    python main.py
    ```

## 📦 Windows (.exe) Oluşturma

Uygulamayı tek bir yürütülebilir dosya (.exe) haline getirmek için aşağıdaki adımları izleyin:

1.  **PyInstaller'ı Yükleyin:**

    ```bash
    pip install pyinstaller
    ```

2.  **Build Komutu:**
    Aşağıdaki komut, uygulamayı tüm bağımlılıklarıyla birlikte tek bir dosyada toplar ve konsol penceresini gizler:
    ```bash
    pyinstaller --noconfirm --onefile --windowed --name "AuraSpeedTest" --add-data "venv/Lib/site-packages/customtkinter;customtkinter/" --icon "icon.ico" main.py
    ```
    _(Not: `icon.ico` dosyanız varsa `--icon` parametresini kullanın, yoksa bu kısmı çıkarabilirsiniz.)_

## 📁 Proje Yapısı

```text
internet_speed_test/
├── main.py             # Ana uygulama dosyası
├── README.md           # Proje dokümantasyonu
├── requirements.txt    # Gerekli kütüphaneler listesi
└── .gitignore          # Git tarafından yoksayılacak dosyalar
```

## 🚀 GitHub Release & Dağıtım

Geliştirdiğiniz `.exe` dosyasını GitHub üzerinde paylaşmak için:

1.  GitHub deponuzda **Releases** bölümüne gidin.
2.  **Draft a new release** butonuna tıklayın.
3.  Versiyon numarasını (örn: `v1.0.0`) belirleyin.
4.  `dist/` klasörü içinde oluşan `AuraSpeedTest.exe` dosyasını sürükleyip bırakarak yükleyin.
5.  **Publish release** diyerek paylaşın.

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
