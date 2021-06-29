import qrcode

data = "http://ogabekrashidov.pythonanywhere.com/"
filename = "portfo.png"

img = qrcode.make(data)
img.save(filename)