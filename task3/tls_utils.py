from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes, hmac
import os, time

def PseudoRandomFunction(secret, label, seed, len) -> bytes:
    # PRF(secret, label, seed) = P_<hash>(secret, label + seed)
    return P_hash(secret, label + seed, len, HMAC_SHA256)

def P_hash(secret, seed, len, hmac):
    hash_len = 32
    n = (len + hash_len - 1) // hash_len

    res = b''
    a = HMAC_SHA256(secret, seed)

    while n > 0:
        res += HMAC_SHA256(secret, a + seed)
        a = HMAC_SHA256(secret, a)
        n -= 1

    return res[:len]

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

def LoadPublicKeyPemFile(filename):
    return serialization.load_pem_public_key(open(filename, 'rb').read(), backend=default_backend())

def LoadPrivateKeyPemFile(filename):
    return serialization.load_pem_private_key(open(filename, 'rb').read(), password=None, backend=default_backend())

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