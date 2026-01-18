from PIL import Image
import os

img = Image.open("logo.png")
# İkon boyutları (Windows standartları)
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
img.save("icon.ico", sizes=icon_sizes)
print("İkon başarıyla oluşturuldu: icon.ico")
