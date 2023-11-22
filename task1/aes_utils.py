from Crypto.Cipher import AES

AES_BLOCK_SIZE = 16

def aes_encryption(input_bytes: bytes, key_bytes: bytes) -> bytes: 
    if len(input_bytes) != 16 or len(key_bytes) != 16:
        raise ValueError("Both input and key must be 128 bits (16 bytes)")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    cipher_text = cipher.encrypt(input_bytes)
    return cipher_text

def aes_decryption(input_bytes: bytes, key_bytes: bytes) -> bytes:
    if len(input_bytes) != 16 or len(key_bytes) != 16:
        raise ValueError("Both input and key must be 128 bits (16 bytes)")
    cipher = AES.new(key_bytes, AES.MODE_ECB)
    cipher_text = cipher.decrypt(input_bytes)
    return cipher_text

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for (x, y) in zip(a, b)])

