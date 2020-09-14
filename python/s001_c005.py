# File name: s001_c004.py
# Description: Cryptopals Set 1, Challenge 5 - Implement repeating-key XOR
# Author: Arya Muralidharan
# Date: 2020-09-08


#---MODULES---#
# N/A


#---CONSTANTS---#
INPUT = "Burning 'em, if you ain't quick and nimble\n" \
    "I go crazy when I hear a cymbal"
KEY = "ICE"
EXPECTED = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272" \
    "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


#---FUNCTIONS---#
def implement_repeating_xor(string, key):
    '''
    Encrypts text using repeating-key XOR.

    Inputs: 
        string: the string to encrypt (str)
        key: the key to encrypt with (str)

    Returns: the encrypted hexstring (str)
    '''
    encoded = []
    i = 0
    for b in string:
        encoded.append(ord(key[i]) ^ ord(b))
        i = i + 1 if i < len(key) - 1 else 0

    return bytes(encoded).hex()


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    actual_out = implement_repeating_xor(INPUT, KEY)

    print("input:\n%s" % INPUT)
    print("key: %s" % KEY)
    print("expected output: %s" % EXPECTED)
    print("actual output: %s" % actual_out)

    if actual_out == EXPECTED:
        print("Success!")
    else:
        print("Failure :-(")


#---RUN---#
if __name__ == '__main__':
    main()