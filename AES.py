from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os


# -------------------------------
# Generate random AES key (256-bit)
# -------------------------------
def generate_key():
    return os.urandom(32)   # 32 bytes = 256 bits


# -------------------------------
# Encrypt function
# -------------------------------
def encrypt_message(key, plaintext):

    iv = os.urandom(16)   # Initialization Vector (16 bytes)

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    encryptor = cipher.encryptor()

    # Padding (AES requires block size of 16 bytes)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    return iv, ciphertext


# -------------------------------
# Decrypt function
# -------------------------------
def decrypt_message(key, iv, ciphertext):

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    decryptor = cipher.decryptor()

    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

    return plaintext.decode()


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":

    key = generate_key()
    message = "Hello! This is AES encryption in Python."

    print("Original Message:", message)

    iv, encrypted_text = encrypt_message(key, message)
    print("Encrypted:", encrypted_text)

    decrypted_text = decrypt_message(key, iv, encrypted_text)
    print("Decrypted:", decrypted_text)
