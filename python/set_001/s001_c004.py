# File name: s001_c004.py
# Description: Cryptopals Set 1, Challenge 4 - Single-byte XOR cipher
# Author: Arya Muralidharan
# Date: 2020-09-08

#---MODULES---#
import s001_c003, urllib.request


#---CONSTANTS---#
URL = "https://cryptopals.com/static/challenge-data/4.txt"


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
    decodings = []
    for l in file:
        x = l.decode()
        key, msg, score = s001_c003.find_key(x)
        temp = {
            'msg': msg,
            'score': score,
            'key': key,
            'line': x
        }
        decodings.append(temp)
    
    decodings.sort(key = lambda x: x['score'], reverse = True)
    best = decodings[0]

    key = best['key']
    message = best['msg']
    score = best['score']
    line = best['line']

    return key, message, score, line


def main():
    '''
    Runs and tests the program.

    Inputs: none

    Returns: none
    '''
    f = urllib.request.urlopen(URL)
    key, message, score, line = detect_xor_line(f)
    message = message.decode()
    print("line: %skey: %d\nmessage: %sscore: %s" % (line, key, message, score))


#---RUN---#
if __name__ == '__main__':
    main()