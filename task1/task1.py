from aes_utils import *

key = bytearray.fromhex('2b7e151628aed2a6abf7158809cf4f3c') # generate your own 16 bytes key
iv = bytearray.fromhex('000102030405060708090a0b0c0d0e0f') # generate your own 16 bytes initial vector

# fill these two functions
def ccbc_encryption(plain: bytes, key: bytes, iv: bytes) -> bytes:
    return None

def ccbc_decryption(cipher: bytes, key: bytes, iv: bytes) -> bytes:
    return None


plaintext = bytes('Thank you so much for your hard work during the 23 Fall semester', 'utf-8')
expected_ciphertext = bytes.fromhex('cf62ae1132f76bb9837e478296ce4e4c0bb2712c2bcc088c24611e264f6178c416f4d8a27f909c0056532ef0193d52bd7893a735fae9e785efdee63547f0269c')
assert(ccbc_encryption(plaintext, key, iv) == expected_ciphertext)
assert(ccbc_decryption(expected_ciphertext, key, iv) == plaintext)
