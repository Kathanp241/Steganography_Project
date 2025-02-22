import cv2

# Read the encrypted image
img = cv2.imread("encryptedImage.png")  # Read PNG to avoid compression issues

# Read the stored password and message length
try:
    with open("secret.txt", "r") as f:
        stored_password = f.readline().strip()  
        stored_msg_length = int(f.readline().strip())  
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Input the decryption password
pas = input("Enter passcode for Decryption: ")

# Check if the password matches
if pas == stored_password:
    message = ""
    
    # ASCII decoding dictionary
    c = {i: chr(i) for i in range(255)}

    index = 0
    for i in range(img.shape[0]): 
        for j in range(img.shape[1]):  
            if index < stored_msg_length:
                message += c[img[i, j, 0]]  
                index += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
