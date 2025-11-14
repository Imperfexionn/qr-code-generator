# Basically a QR code generator thingy. 💚
# Reminder: make sure you installed qrcode + PIL, otherwise this will throw a tantrum.
# Do so by typing >> pip install qrcode[pil] in your terminal.

import os  # for handling folders and paths like a pro.
import qrcode  # the magical QR code maker.

# ask the user for the URL they want to turn into a QR code.
user_url = input("Enter the URL that you want to transfigure into a QR code: ").strip()

# ask for a name for the QR code file, because default names are boring.
qr_name = input("Enter the QR code name: ")
if qr_name == "":  # if they leave it blank, we'll just be classy and call it "qr code".
    qr_name = "qr code"
qr_name = qr_name + ".png"  # append .png so we can actually open it in an image viewer.

# decide where we want to put this QR code (Documents/QR Codes folder).
qr_folder = os.path.join(os.path.expanduser("~"), "Documents", "QR Codes")
os.makedirs(qr_folder, exist_ok=True)  # make the folder if it doesn't exist, otherwise chill.

# full path to the file including the name, so Python knows exactly where to save it.
full_file_path = os.path.join(qr_folder, qr_name)

# time to make the QR code object, basically the blueprint of our future QR.
qr = qrcode.QRCode()
qr.add_data(user_url)  # feed it the URL we want to encode.
qr_code_img = qr.make_image()  # turn the blueprint into an actual image.

# save it to the folder we prepared earlier, voila! QR magic done!
qr_code_img.save(full_file_path)

# success! tell the user where their masterpiece ended up! ^-^

print(f"All done! Your QR code has been safely stored at:\n{full_file_path}")
