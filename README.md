# **SECURE DATA HIDING IN IMAGE USING STEGANOGRAPHY**

**INTRODUCTION:**

Ever wanted to send secret message without drawing any attention?
This Project lets you implement the image-based steganography, by hiding the messages within images. Steganography add's an extra layer of the invisibility that old traditional can't provide.It can be only access by the authorise person who have pass key to unlock the file.

**HOW IT WORKS:**

**Encryption (Hiding the Message)**

The user enters a secret message and a password.</br>
The message is embedded inside an image at the pixel level.</br>
The modified image is saved and looks just like the original.

**Decryption (Revealing the Message)**

The user enters the password.</br>
The program extracts the hidden message from the image.</br>
If the password is correct, the secret message is revealed!</br>

**INSTALLATION & USAGE:**

Install Dependencies

We have to ensure that Python is installed, then install OpenCV

**pip install opencv-python**

**RUN THE ENCRYPTION FILE**

File Name: **encrypt1.py**</br>
Whenever you run the file, Pop-up will show to enter the secret message and password to encrypt.</br>
An encrypted image file (encryptedimage.jpg) will be created.

**RUN THE DECRYPTION FILE**

File Name: **decrypt1.py**</br>
Enter the password to unlock the secret message.

![image](https://github.com/user-attachments/assets/2accae6e-3a8f-416d-9f45-8d22dd483166)

**FEATURES:**

**Invisible Encryption:** </br>
The image looks untouched even after the message is hidden.

**Password-Protected:**</br>
Only users with the correct passcode can decrypt the hidden text.

**Lightweight & Fast:**</br>
No heavy dependencies, just OpenCV for image processing.

**Supports Multiple Formats:** </br>
Works with JPEG, PNG, BMP, and more without quality loss.


**PROJECT STRUCTURE:**

📂 **Steganography-Project:**

 ├── encrypt.py  # Script to hide messages inside images</br> 
 ├── decrypt.py  # Script to extract hidden messages</br> 
 ├── encryptedImage.jpg  # Sample encrypted image</br> 
 ├── README.md  # Project documentation







