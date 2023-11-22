from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes, hmac
import os, time

def GenerateKeyPairPem():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def LoadPublicKeyPem(public_key_pem):
    return serialization.load_pem_public_key(public_key_pem, backend=default_backend())

def LoadPrivateKeyPem(private_key_pem):
    return serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())

def Encrypt(message, public_key):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def Decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

def SHA256(bytes):
    sha256_hash = hashes.Hash(hashes.SHA256(), backend=default_backend())
    sha256_hash.update(bytes)
    return sha256_hash.finalize()

def HMAC_SHA256(key, bytes):
    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(bytes)
    return h.finalize()

def GenerateRandomBytes(length):
    return os.urandom(length)

def GetTimestamp():
    return int(time.time())