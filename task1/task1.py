from aes_utils import *
from Crypto.Random import get_random_bytes

# key = bytearray.fromhex('2b7e151628aed2a6abf7158809cf4f3c') # generate your own 16 bytes key
# iv = bytearray.fromhex('000102030405060708090a0b0c0d0e0f') # generate your own 16 bytes initial vector

def generate_random_key_iv():
    key = bytearray(get_random_bytes(16))  # 16 bytes = 128 bits
    iv = bytearray(get_random_bytes(16))   # 16 bytes = 128 bits
    return key, iv

key, iv = generate_random_key_iv()

# fill these two functions
def ccbc_encryption(plain: bytes, key: bytes, iv: bytes) -> bytes:
    input_list = [plain[i:i+AES_BLOCK_SIZE] for i in range(0, len(plain), AES_BLOCK_SIZE)]
    encrypted_blocks = []

    carry_in = None
    while(len(input_list)!=0):
        if(carry_in == None):
            carry_in = iv
        plain_input = input_list.pop(0)
        block_input = xor_bytes(plain_input, carry_in)
        block_output = aes_encryption(block_input, key)
        ciper = xor_bytes(block_output, carry_in)
        carry_in = xor_bytes(plain_input, ciper)
        # bytes concatenate
        encrypted_blocks.append(ciper)
        
    return  b''.join(encrypted_blocks)

def ccbc_decryption(cipher: bytes, key: bytes, iv: bytes) -> bytes:
    input_list = [cipher[i:i+AES_BLOCK_SIZE] for i in range(0, len(cipher), AES_BLOCK_SIZE)]
    carry_in = None
    decrypted_blocks = []

    while(len(input_list)!=0):
        if(carry_in==None):
            carry_in = iv
        cipher_input = input_list.pop(0)
        block_input = xor_bytes(cipher_input, carry_in)
        block_output = aes_decryption(block_input, key)
        plain = xor_bytes(block_output, carry_in)
        carry_in = xor_bytes(cipher_input, plain)
        decrypted_blocks.append(plain)

    return b''.join(decrypted_blocks)

plaintext = bytes('Thank you so much for your hard work during the 23 Fall semester', 'utf-8')
expected_ciphertext = bytes.fromhex('cf62ae1132f76bb9837e478296ce4e4c0bb2712c2bcc088c24611e264f6178c416f4d8a27f909c0056532ef0193d52bd7893a735fae9e785efdee63547f0269c')
assert(ccbc_encryption(plaintext, key, iv) == expected_ciphertext)
assert(ccbc_decryption(expected_ciphertext, key, iv) == plaintext)
