# importing pyqrcode module to generate the qrcode
import pyqrcode
# importing
import png

qr = pyqrcode.create("https://www.youtube.com/PROGRAMMINGHERO1010")
qr.png("qr-code.png")
