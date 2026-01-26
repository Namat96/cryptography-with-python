
import random
import math


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Generate a random prime number
def generate_prime(start=50, end=200):
    while True:
        num = random.randint(start, end)
        if is_prime(num):
            return num


# Extended Euclidean Algorithm
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None


# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


# Encryption
def encrypt(message, public_key):
    e, n = public_key
    cipher = []

    for char in message:
        cipher.append(pow(ord(char), e, n))

    return cipher


# Decryption
def decrypt(cipher, private_key):
    d, n = private_key
    message = ""

    for num in cipher:
        message += chr(pow(num, d, n))

    return message


# -------- MAIN PROGRAM --------

print("RSA Cryptography Program")
print("------------------------")

public_key, private_key = generate_keys()

print("Public Key:", public_key)
print("Private Key:", private_key)

message = input("\nEnter message: ")

encrypted_message = encrypt(message, public_key)
print("\nEncrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
