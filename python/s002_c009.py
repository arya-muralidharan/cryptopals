# File name: s002_c009.py
# Description: Cryptopals Set 2, Challenge 9 - Implement PKCS#7 padding
# Author: Arya Muralidharan
# Date: 2020-09-28

#---MODULES---#
from Crypto.Util.Padding import pad


#---CONSTANTS---#
INPUT_1 = "YELLOW SUBMARINE"
INPUT_2 = 20
EXPECTED = "YELLOW SUBMARINE\x04\x04\x04\x04"


#---FUNCTIONS---#
def pkcs7_padding(text, num):
    '''
    Pad to a specific block length using the PKCS#7 padding scheme.

    Inputs: 
        text: the text (str)
        num: the number of bytes to pad (int)

    Returns:  the padded string (str)
    '''
    return pad(text.encode(), num).decode()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    actual_out = pkcs7_padding(INPUT_1, INPUT_2)
    print("INPUT 1: ", INPUT_1)
    print("INPUT 2: ", INPUT_2)
    print("EXPECTED OUTPUT: %s" % EXPECTED)
    print("ACTUAL OUTPUT: %s" % actual_out)

    if actual_out == EXPECTED:
        print("SUCCESS!")
    else:
        print("FAILURE :-(")
    

#---RUN---#
if __name__ == '__main__':
    main()