# File name: s001_c007.py
# Description: Cryptopals Set 1, Challenge 7 - AES in ECB mode
# Author: Arya Muralidharan
# Date: 2020-09-20


#---MODULES---#
from base64 import b64decode
from urllib.request import urlopen
from Crypto.Cipher import AES # pip install pycryptodome


#---CONSTANTS---#
URL = "https://cryptopals.com/static/challenge-data/7.txt"
TEXT = urlopen(URL).read()
KEY = "YELLOW SUBMARINE"


#---FUNCTIONS---#
def break_aes_ecb(text, key):
    '''
    Breaks the encryption on a text that has been encrypted as follows:
        (1) AES-128 in ECB mode
        (2) Base64

    Inputs: 
        text: the encrypted text (str or bytes)
        key: the key used to AES-encrypt (str)

    Returns: the decoded message (str)
    '''
    data = b64decode(text)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    message = cipher.decrypt(data)

    return message.decode()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    message = break_aes_ecb(TEXT, KEY)
    print("MESSAGE:\n%s" % message)


#---RUN---#
if __name__ == '__main__':
    main()