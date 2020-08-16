# File name: s001_c001.py
# Description: Cryptopals Set 1, Challenge 1 - Convert hex to base64
# Author: Arya Muralidharan
# Date: 2020-08-13

# Cryptopals Rule: 
# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing.

#---MODULES---#
import base64


#---CONSTANTS---#
TEST = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
EXPECTED_OUT = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


#---FUNCTIONS---#
def hex_to_base64(str):
    '''
    Converts hex to base64.

    Inputs: 
        str: a string (in hex)

    Returns: a string (in base64)
    '''
    decoded = base64.b16decode(str, casefold=True)
    encoded = base64.b64encode(decoded) # encoded is now class 'bytes'

    return encoded.decode()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    actual_out = hex_to_base64(TEST)

    print("input: ", TEST)
    print("expected output: ", EXPECTED_OUT)
    print("actual output: ", actual_out)

    if actual_out == EXPECTED_OUT:
        print("Success!")
    else:
        print("Failure :-(")


#---RUN---#
if __name__ == '__main__':
    main()