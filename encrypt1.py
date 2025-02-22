
import cv2
import os
import string

# Read the image
img = cv2.imread("Lambo.jpeg")  

# Input the message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Save password and message length to a file
with open("secret.txt", "w") as f:
    f.write(password + "\n")  
    f.write(str(len(msg)) + "\n")  

# ASCII encoding dictionary
d = {chr(i): i for i in range(255)}

index = 0
for i in range(img.shape[0]):  
    for j in range(img.shape[1]):  
        if index < len(msg):
            img[i, j, 0] = d[msg[index]]  
            index += 1

# Save the encrypted image as PNG to prevent compression issues
cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.jpg")  

print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")
