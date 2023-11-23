from aes_utils import *

key = bytearray.fromhex('2b7e151628aed2a6abf7158809cf4f3c') # generate your own 16 bytes key
iv = bytearray.fromhex('000102030405060708090a0b0c0d0e0f') # generate your own 16 bytes initial vector

# fill these two functions and submit this file
def ccbc_encryption(plain: bytes, key: bytes, iv: bytes) -> bytes:
    return None

def ccbc_decryption(cipher: bytes, key: bytes, iv: bytes) -> bytes:
    return None
