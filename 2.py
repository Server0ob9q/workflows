from cryptography.fernet import Fernet

def get_hwid():
    hwid = uuid.getnode()
    return hwid

def load_hwid_from_github():
    with open('hwid.txt', 'rb') as hwid_file:
        encrypted_hwid = hwid_file.read()
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return encrypted_hwid, key

def verify_hwid():
    current_hwid = get_hwid()
    encrypted_hwid, key = load_hwid_from_github()
    cipher = Fernet(key)
    decrypted_hwid = cipher.decrypt(encrypted_hwid).decode()
    return current_hwid == int(decrypted_hwid)

if __name__ == "__main__":
    if verify_hwid():
        print("HWID verification succeeded.")
    else:
        print("HWID verification failed.")
