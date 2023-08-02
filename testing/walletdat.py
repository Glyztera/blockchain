import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import urlsafe_b64encode, urlsafe_b64decode

def encrypt(data, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()

    return urlsafe_b64encode(salt + iv + ciphertext).decode('utf-8')

def decrypt(encrypted_data, password):
    decoded_data = urlsafe_b64decode(encrypted_data.encode())
    salt, iv, ciphertext = decoded_data[:16], decoded_data[16:32], decoded_data[32:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode('utf-8')

# Save to wallet.dat
wallet_data = {
    'private_key': private_pem.decode(),
    'public_key': public_pem.decode()
}
encrypted_wallet = encrypt(json.dumps(wallet_data), "your_password")
with open("wallet.dat", "w") as f:
    f.write(encrypted_wallet)

# Load from wallet.dat
with open("wallet.dat", "r") as f:
    encrypted_data = f.read()
wallet_data = json.loads(decrypt(encrypted_data, "your_password"))
