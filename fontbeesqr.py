import qrcode
import os
from PIL import Image

def generate_qr(url, filename="qrcode.png"):
    """
    Generates a QR code from the given URL and saves it as an image file.

    Parameters:
    url (str): The URL to encode in the QR code.
    filename (str): The name of the file to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

    # Display the QR Code
    img.show()

def display_fontbees_name():
    """
    Displays the company name "FontBees" in green color with a stylized format.
    """
    print("\033[92m--==[ FontBees ]==--\033[0m")  # \033[92m is the ANSI escape code for green

def main():
    """
    Main function that runs the QR code generator tool.
    """
    display_fontbees_name()  # Display "FontBees" when the tool is activated

    # Always ask for the URL
    url = input("Enter the URL to generate QR Code: ")

    generate_qr(url)

if __name__ == "__main__":
    main()
