# File name: s001_c008.py
# Description: Cryptopals Set 1, Challenge 8 - Detect AES in ECB mode
# Author: Arya Muralidharan
# Date: 2020-09-26

#---MODULES---#
from urllib.request import urlopen


#---CONSTANTS---#
URL = "https://cryptopals.com/static/challenge-data/8.txt"
TEXT = urlopen(URL).read()


#---FUNCTIONS---#
def detect_aes_ecb(text):
    '''
    Detect the hex-encoded ECB-encrypted string in a text.

    Inputs: 
        text: the text (str)

    Returns: a tuple
        num: the line number (int)
        line: the ECB-encrypted string (str)
    '''
    max_dupes = 0
    line = ""
    num = 0
    
    for i, l in enumerate(text.splitlines()):
        blocks = [l[j:j+16] for j in range(0, len(l), 16)]
        num_dupes = len(blocks) - len(set(blocks))
        if (num_dupes > max_dupes):
            max_dupes = num_dupes
            line = l.decode()
            num = i+1
    
    return num, line


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    no, line = detect_aes_ecb(TEXT)
    print("LINE %d: %s" % (no, line))


#---RUN---#
if __name__ == '__main__':
    main()