# File name: s001_c003.py
# Description: Cryptopals Set 1, Challenge 3 - Single-byte XOR cipher
# Author: Arya Muralidharan
# Date: 2020-09-07

#---MODULES---#
# N/A


#---CONSTANTS---#
TEST = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


#---FUNCTIONS---#
def phrase_score(b_input):
    '''
    Calculate the English score of a string using letter and space frequency.
    (H/t https://en.wikipedia.org/wiki/Letter_frequency.)

    Inputs: 
        str: a string (in hex)

    Returns: an int ()
    '''
    freq = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02260, 'x': 0.00150, 'y': 0.01974,
        'z': 0.00074, ' ': 0.19000
        }
    
    return sum([freq.get(chr(b), 0) for b in b_input.lower()])


def find_key(str):
    '''
    Find the key used to XOR-encrypt a given hex string.

    Inputs: 
        str: a string (in hex)

    Returns: a tuple
        key: the key (int)
        message: the decrypted message (bytestring)
        score: the frequency score (float)
    '''
    b_str = bytes.fromhex(str)
    decodings = []
    for i in range(256):
        msg = bytes([b ^ i for b in b_str])
        score = phrase_score(msg)
        temp = {
            'msg': msg,
            'score': score,
            'key': i
        }
        decodings.append(temp)
    
    decodings.sort(key = lambda x: x['score'], reverse = True)
    best = decodings[0]

    key = best['key']
    message = best['msg']
    score = best['score']

    return key, message, score


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    key, message, score = find_key(TEST)
    message = message.decode()
    print("key: %d\nmessage: %s\nscore: %s" % (key, message, score))


#---RUN---#
if __name__ == '__main__':
    main()