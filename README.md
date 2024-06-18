# caesar-cipher
Python program that can encrypt and decrypt text using the Caesar Cipher algorithm

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Get the initial message and shift values from the user
initial_message = input("Enter initial message: ")
encrypt_shift = int(input("Enter shift value for encryption: "))

# Encrypt the initial message
encrypted_message = caesar_cipher(initial_message, encrypt_shift)
print("Encrypted message:", encrypted_message)

# Decrypt the encrypted message using the negative of the encryption shift
decrypted_message = caesar_cipher(encrypted_message, -encrypt_shift)
print("Decrypted message:", decrypted_message)

print("Decryption successful:", initial_message == decrypted_message)

#OUTPUT
#Initail message
![Screenshot 2024-06-18 203925](https://github.com/Ajay0072005/caesar-cipher/assets/173068768/2f5440f8-2fdd-4fc9-ac90-0de8b78ee5ab)

#Shift key value
![Screenshot 2024-06-18 203942](https://github.com/Ajay0072005/caesar-cipher/assets/173068768/82121172-0ce0-49d1-a451-9b570c6f8024)

#Final Output
![Screenshot 2024-06-18 203959](https://github.com/Ajay0072005/caesar-cipher/assets/173068768/1c2d4412-8754-430d-805e-e2adc78dae8b)



