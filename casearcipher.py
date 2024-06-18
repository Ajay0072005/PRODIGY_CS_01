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


