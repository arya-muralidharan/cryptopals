# File name: s002_c010.py
# Description: Cryptopals Set 2, Challenge 10 - Implement CBC mode
# Author: Arya Muralidharan
# Date: 2021-06-28

#---MODULES---#
from base64 import b64decode
from urllib.request import urlopen
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#---CONSTANTS---#
URL = "https://cryptopals.com/static/challenge-data/10.txt"
TEXT = urlopen(URL).read()
KEY = b'YELLOW SUBMARINE'
IV = b'\x00' * AES.block_size


#---FUNCTIONS---#
def encrypt_aes_cbc(mtxt, key, initval):
    '''
    Encrypts a message using AES-CBC

    Inputs: 
        mtxt: the message to encrypt (str or bytes)
        key: the key used to AES-encrypt (str)
        iv: the initial value for CBC encryption

    Returns: the decoded message (bytes)
    '''
      
    msg = pad(mtxt.encode(), AES.block_size)
    prev_block = initval
    ciphertext = b''

    for i in range(0, len(msg), AES.block_size):
        block = msg[i:i+AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv=prev_block)
        ciphertext += cipher.encrypt(block)
        prev_block = block
    
    return ciphertext


def decrypt_aes_cbc(ctxt, key, iv):
    '''
    Breaks the encryption on an AES-CBC-encoded text

    Inputs: 
        ctxt: the encrypted text (str or bytes)
        key: the key used to AES-encrypt (str)
        iv: the initial value for CBC encryption

    Returns: the decoded message (bytes)
    '''
    
    prev_block = iv
    plaintext = b''

    for i in range(0, len(ctxt), AES.block_size):
        block = ctxt[i:i+AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv=prev_block)
        plaintext += cipher.decrypt(block)
        prev_block = block
    
    return unpad(plaintext, AES.block_size)


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    data = b64decode(TEXT)
    dec = decrypt_aes_cbc(data, KEY, IV)
    print("MESSAGE:\n%s" % dec.decode())
    

#---RUN---#
if __name__ == '__main__':
    main()