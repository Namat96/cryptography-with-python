"""
Hybrid Cryptography System
Combines RSA (for key exchange) and AES (for data encryption)

Author: Namat Ullah
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64


# -------------------------------
# RSA KEY GENERATION
# -------------------------------

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


# -------------------------------
# AES ENCRYPTION
# -------------------------------

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return cipher.nonce, ciphertext, tag


def aes_decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode()


# -------------------------------
# HYBRID ENCRYPTION
# -------------------------------

def hybrid_encrypt(message, public_key):
    aes_key = get_random_bytes(16)

    rsa_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    nonce, ciphertext, tag = aes_encrypt(message, aes_key)

    return encrypted_aes_key, nonce, ciphertext, tag


def hybrid_decrypt(encrypted_aes_key, nonce, ciphertext, tag, private_key):
    rsa_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)

    plaintext = aes_decrypt(nonce, ciphertext, tag, aes_key)
    return plaintext


# -------------------------------
# MAIN PROGRAM
# -------------------------------

def main():
    print("\n--- HYBRID CRYPTOGRAPHY SYSTEM (RSA + AES) ---\n")

    private_key, public_key = generate_rsa_keys()

    message = input("Enter a message to encrypt: ")

    encrypted_aes_key, nonce, ciphertext, tag = hybrid_encrypt(message, public_key)

    print("\nEncrypted Message (Base64):")
    print(base64.b64encode(ciphertext).decode())

    decrypted_message = hybrid_decrypt(
        encrypted_aes_key, nonce, ciphertext, tag, private_key
    )

    print("\nDecrypted Message:")
    print(decrypted_message)


if __name__ == "__main__":
    main()
