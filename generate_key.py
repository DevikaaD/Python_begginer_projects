from cryptography.fernet import Fernet

# Generate a key and save it to a file
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

