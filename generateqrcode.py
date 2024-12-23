import qrcode

data = "https://www.youtube.com/@python_buzz"

qr = qrcode.make(data)

qr.save("pythonbuzz_qr.png")

print("QR is generated successfully")