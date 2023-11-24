from aes_utils import *

key = bytearray.fromhex('2b7e151628aed2a6abf7158809cf4f3c') # generate your own 16 bytes key
iv = bytearray.fromhex('000102030405060708090a0b0c0d0e0f') # generate your own 16 bytes initial vector

# fill these two functions
def ccbc_encryption(plain: bytes, key: bytes, iv: bytes) -> bytes:
    return None

def ccbc_decryption(cipher: bytes, key: bytes, iv: bytes) -> bytes:
    return None


plaintext = bytes('Thank you so much for your hardwork during the 23 Fall semester.', 'utf-8')
expected_ciphertext = bytes.fromhex('cf62ae1132f76bb9837e478296ce4e4ce2a07c5165df9ceb3f3633b55e5a18a33f61960126df5fe5eb7b6365f830bb41a3e39f674741bc1d24854152cbe0a43c')
assert(ccbc_encryption(plaintext, key, iv) == expected_ciphertext)
assert(ccbc_decryption(expected_ciphertext, key, iv) == plaintext)
