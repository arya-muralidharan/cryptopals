# File name: s001_c002.py
# Description: Cryptopals Set 1, Challenge 2 - Fixed XOR
# Author: Arya Muralidharan
# Date: 2020-09-07

# Cryptopals Rule: 
# Always operate on raw bytes, never on encoded strings. 
# Only use hex and base64 for pretty-printing.

#---MODULES---#


#---CONSTANTS---#
INPUT_1 = "1c0111001f010100061a024b53535009181c"
INPUT_2 = "686974207468652062756c6c277320657965"
EXPECTED_OUT = "746865206b696420646f6e277420706c6179"


#---FUNCTIONS---#
def fixed_xor(str1, str2):
    '''
    Takes two equal-length buffers and produces their XOR combination.

    Inputs: 
        str1: a string (in hex)
        str2: a string (in hex)

    Returns: a string (in hex)
    '''
    b_str1 = bytes.fromhex(str1)
    b_str2 = bytes.fromhex(str2)

    xord = bytes([b1 ^ b2 for b1, b2 in zip(b_str1, b_str2)])

    return xord.hex()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    actual_out = fixed_xor(INPUT_1, INPUT_2)

    print("input 1: ", INPUT_1)
    print("input 2: ", INPUT_2)
    print("expected output: ", EXPECTED_OUT)
    print("actual output: ", actual_out)

    if actual_out == EXPECTED_OUT:
        print("Success!")
    else:
        print("Failure :-(")


#---RUN---#
if __name__ == '__main__':
    main()