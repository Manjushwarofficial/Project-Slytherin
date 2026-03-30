import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# The key is securely generated and rotated, never stored on disk.
SECRET_KEY = os.urandom(32)

def secure_blueprint(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    # Pad data to 16-byte boundaries
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    # Encrypting using AES
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    
    with open(filepath + ".enc", "wb") as f:
        f.write(encrypted_data)
        
# secure_blueprint("vault_blueprint.bmp")
