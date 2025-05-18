from cryptography.fernet import Fernet

#load key
def load_key():
    with open("encryption.key", "rb") as f:
        return f.read()

#encrypt given file
def encrypt_file(path):
    key = load_key()
    fernet = Fernet(key)
    with open(path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(path, "wb") as file:
        file.write(encrypted)

# Decrypt and return contents of a file
def decrypt_file(path):
    key = load_key()
    fernet = Fernet(key)

    with open(path, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)
    with open(path, "wb") as file:
        file.write(decrypted)