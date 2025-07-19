# Reverse Cipher: Encrypt or Decrypt based on user input

def reverse_cipher(text):
    return text[::-1]

# Ask user for input
message = input("Enter your message (plain text or cipher text): ")

# Reverse the message to encrypt or decrypt
result = reverse_cipher(message)

print("\nConverted message:")
print(result)
