from cryptography.fernet import Fernet


def read_file(file_path):
    with open(file_path, 'r') as file:
        return "".join(file.readlines())


def generate_key():
    KEY = Fernet.generate_key()
    return KEY


def encrypt_file(t, k):
    fernet = Fernet(k)
    return fernet.encrypt(bytes(t, 'utf-8'))


def decrypt_file(token, k):
    fernet = Fernet(k)
    return fernet.decrypt(token)


FILE_PATH = "text.txt"
ORIGINAL_TEXT = read_file(FILE_PATH)
print("Initial text:\n", ORIGINAL_TEXT)

KEY = generate_key()

ENCRYPTED_TEXT = encrypt_file(ORIGINAL_TEXT, KEY)
print("Encrypted file:\n", ENCRYPTED_TEXT)

decrypted = decrypt_file(ENCRYPTED_TEXT, KEY)
print("Decrypted file:\n", decrypted)