SECURE DATA HIDING IN IMAGE USING STEGANOGRAPHY

INTRODUCTION:
Ever wanted to send secret message without drawing any attention?
This Project lets you implement the image-based steganography, by hiding the messages within images. Steganography add's an extra layer of the invisibility that old traditional can't provide.It can be only access by the authorise person who have pass key to unlock the file.

HOW IT WORKS:
Encryption (Hiding the Message)
The user enters a secret message and a password.

The message is embedded inside an image at the pixel level.

The modified image is saved and looks just like the original.

Decryption (Revealing the Message)
The user enters the password.

The program extracts the hidden message from the image.

If the password is correct, the secret message is revealed!

INSTALLATION & USAGE:
Install Dependencies
We have to ensure that Python is installed, then install OpenCV

pip install opencv-python

RUN THE ENCRYPTION FILE
File Name: encrypt1.py
Whenever you run the file, Pop-up will show to enter the secret message and password to encrypt.
An encrypted image file (encryptedimage.jpg) will be created.

RUN THE DECRYPTION FILE
File Name:decrypt1.py
Enter the password to unlock the secret message.





