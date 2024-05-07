# import pyqrcode
# from pyqrcode import QRCode

# # String which represents the QR code
# s = "https://www.youtube.com/watch?v=6-kWW9wJ3o0"

# # Generate QR code
# url = pyqrcode.create(s)

# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)

import qrcode as code

img = code.make("https://www.youtube.com/watch?v=6-kWW9wJ3o0")

img.save("myqr.png")