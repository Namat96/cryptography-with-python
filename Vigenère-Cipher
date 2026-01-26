
def generate_key(message, key):
    key = key.upper()
    key_list = []
    j = 0

    for i in range(len(message)):
        if message[i].isalpha():
            key_list.append(key[j % len(key)])
            j += 1
        else:
            key_list.append(message[i])

    return "".join(key_list)


def encrypt_vigenere(message, key):
    message = message.upper()
    key = generate_key(message, key)
    cipher_text = ""

    for i in range(len(message)):
        if message[i].isalpha():
            x = (ord(message[i]) - 65 + ord(key[i]) - 65) % 26
            cipher_text += chr(x + 65)
        else:
            cipher_text += message[i]

    return cipher_text


def decrypt_vigenere(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = generate_key(cipher_text, key)
    original_text = ""

    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            x = (ord(cipher_text[i]) - 65 - (ord(key[i]) - 65)) % 26
            original_text += chr(x + 65)
        else:
            original_text += cipher_text[i]

    return original_text


# ----------- MAIN PROGRAM -----------

print("Vigenère Cipher Program")
print("-----------------------")

message = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt_vigenere(message, key)
print("\nEncrypted Message:", encrypted)

decrypted = decrypt_vigenere(encrypted, key)
print("Decrypted Message:", decrypted)
