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
def implement_repeating_xor(str, key):
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
    encoded = []
    i = 0
    for b in str:
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