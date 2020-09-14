# File name: s001_c004.py
# Description: Cryptopals Set 1, Challenge 4 - Detect single-character XOR
# Author: Arya Muralidharan
# Date: 2020-09-08

#---MODULES---#
import s001_c003
from urllib.request import urlopen


#---CONSTANTS---#
FILE = urlopen("https://cryptopals.com/static/challenge-data/4.txt")


#---FUNCTIONS---#
def detect_xor_line(file):
    '''
    Find and decrypt the single-character XOR-encrypted string in a file.

    Inputs: 
        file: the file or webpage containing the strings of uniform length

    Returns: a tuple
        key: the key (int)
        message: the decrypted message (bytestring)
        score: the frequency score (float)
        line: the encrypted line (string)
    '''
    max_score = 0.0
    message = b""
    key = 0
    line = ""

    for x in file:
        l = x.decode()
        k, m, s = s001_c003.find_key(l)
        if s > max_score:
            max_score = s
            key = k
            message = m
            line = l
    
    return key, message, max_score, line


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    key, message, score, line = detect_xor_line(FILE)
    message = message.decode()
    print("line: %skey: %d\nmessage: %sscore: %s" % (line, key, message, score))


#---RUN---#
if __name__ == '__main__':
    main()