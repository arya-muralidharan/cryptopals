# File name: s001_c006.py
# Description: Cryptopals Set 1, Challenge 6 - Break repeating-key XOR
# Author: Arya Muralidharan
# Date: 2020-09-14

#---MODULES---#
import s001_c005, s001_c003
from base64 import b64decode
from urllib.request import urlopen


#---CONSTANTS---#
URL = "https://cryptopals.com/static/challenge-data/6.txt"
TEXT = urlopen(URL).read()


#---FUNCTIONS---#
def hamming_distance(str1, str2):
    '''
    Compute the edit/Hamming distance between two equal-length strings.

    Inputs: 
        str1: a string (str)
        str2: another string (str)

    Returns: the number of differing bits (int)
    '''
    dif = [ord(l1) ^ ord(l2) for l1, l2 in zip(str1, str2)]

    dist = 0
    for n in dif:
        while(n):
            dist += n & 1
            n >>= 1  
         
    return dist


def find_key(b_str):
    '''
    Finds the key used to XOR-encrypt a given bytestring.

    Inputs: 
        b_str: a bytestring (bytes)

    Returns: the key (int)
    '''
    max_score = 0.0
    key = 0
    for i in range(256):
        msg = bytes([b ^ i for b in b_str])
        score = s001_c003.phrase_score(msg)
        if score > max_score:
            max_score = score
            key = i

    return key


def find_key_size(text):
    '''
    Finds the (most likely) key size for an XOR-encrypted text.

    Inputs: 
        text: the text (str)

    Returns: the key size (int)
    '''
    best_ndist = 500.0
    best_size = 0
    
    for sz in range(2, 41):
        blocks = [text[i:i+sz] for i in range(0, len(text), sz)]
        edit_dist = 0
        for i in range(len(blocks)-1):
            edit_dist += hamming_distance(blocks[i], blocks[i+1])
        ndist = (edit_dist / (len(blocks)-1)) / sz
        if ndist < best_ndist:
            best_ndist = ndist
            best_size = sz
    
    return best_size


def break_repeating_XOR(text):
    '''
    Breaks the encryption on a text that has been encrypted as follows:
        (1) Repeating-key XOR
        (2) Base64

    Inputs: 
        text: the encrypted text (str or bytes)

    Returns: a tuple
        key: the key (str)
        message: the decoded message (str)
    '''
    decrypted = b64decode(text).decode()
    keysize = find_key_size(decrypted)
    key = ""

    for i in range(keysize):
        block = ''
        for j in range(i, len(decrypted), keysize):
            block += decrypted[j]
        k = find_key(block.encode())
        key += chr(k)

    message = bytes.fromhex(s001_c005.implement_repeating_xor(decrypted, key))

    return key, message.decode()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    key, message = break_repeating_XOR(TEXT)
    print("KEY:\n%s\n\nMESSAGE:\n%s" % (key, message))


#---RUN---#
if __name__ == '__main__':
    main()