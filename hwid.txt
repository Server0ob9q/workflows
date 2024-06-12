import uuid
from cryptography.fernet import Fernet

def get_hwid():
    hwid = uuid.getnode()
    return hwid

def encrypt_hwid(hwid, key):
    cipher = Fernet(key)
    encrypted_hwid = cipher.encrypt(str(hwid).encode())
    return encrypted_hwid

def save_hwid_to_github(hwid, key):
    encrypted_hwid = encrypt_hwid(hwid, key)
    with open('hwid.txt', 'wb') as hwid_file:
        hwid_file.write(encrypted_hwid)

if __name__ == "__main__":
    hwid = get_hwid()
    key = Fernet.generate_key()
    save_hwid_to_github(hwid, key)
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    print(f"HWID: {hwid}")
    print(f"Key: {key.decode()}")
