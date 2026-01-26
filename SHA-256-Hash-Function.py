import hashlib


def sha256_hash(message):
    # Convert message to bytes
    message_bytes = message.encode('utf-8')

    # Create SHA-256 hash object
    hash_object = hashlib.sha256(message_bytes)

    # Get hexadecimal digest
    return hash_object.hexdigest()


def verify_message(original_message, stored_hash):
    # Hash the message again and compare
    return sha256_hash(original_message) == stored_hash


# -------- MAIN PROGRAM --------

print("SHA-256 Hash Function")
print("---------------------")

message = input("Enter message: ")

hashed_value = sha256_hash(message)
print("\nSHA-256 Hash:", hashed_value)

check = input("\nRe-enter message to verify: ")

if verify_message(check, hashed_value):
    print("Hash verified. Message is unchanged.")
else:
    print("Hash mismatch. Message has changed.")
