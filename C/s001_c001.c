/* File name: s001_c001.c
 * Description: Cryptopals Set 1, Challenge 1 - Convert hex to base64
 * Author: Arya Muralidharan
 * Date: 2020-08-14
 * 
 * Cryptopals Rule: 
 * Always operate on raw bytes, never on encoded strings. 
 * Only use hex and base64 for pretty-printing. */


/* LIBRARIES */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* CONSTANTS */
char* TEST = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
char* EXPECTED_OUT = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";


/* FUNCTIONS */
// unhex: convert hex char to int
int unhex(char ch)
{
    if (ch >= '0' && ch <= '9') {
        return ch - '0';
    }      
    else if (ch >= 'A' && ch <= 'F') {
        return ch - 'A' + 10;
    }
    else if (ch >= 'a' && ch <= 'f') {
        return ch - 'a' + 10;
    }      
    return -1;
}

// b16encode: decode hex
void b16decode(char* instr, char* outstr, unsigned inlen) {
    char temp1;
    unsigned j = 0;
    for (unsigned i=0; i < inlen; i+=2) {
        temp1 = (unhex(instr[i]) << 4) | unhex(instr[i+1]);
        outstr[j] = temp1;
        j++;
    }
    outstr[j] = '\0';
}

// b64encode: encode b64
void b64encode(char* instr, char* outstr, unsigned inlen, unsigned outlen) {
    char* b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    char in1, in2, in3;
    unsigned bitstring, j = 0; 

    for (unsigned i=0; i < inlen; i+=3) {
        in1 = instr[i];
        if (instr[i+1]) {
            in2 = instr[i+1];
            if (instr[i+2]) {
                in3 = instr[i+2];
            }
            else {
                in3 = 0;
            }
        }
        else {
            in2 = 0;
            in3 = 0;
        }
        bitstring = (in1 << 16) | (in2 << 8) | in3;

        outstr[j] = b64[(bitstring >> 18) & 0x3F];
        outstr[++j] = b64[(bitstring >> 12) & 0x3F];

        if (++j < outlen + 1) {
            outstr[j] = b64[(bitstring >> 6) & 0x3F];
            if (++j < outlen + 1) {
                outstr[j] = b64[bitstring & 0x3F];
            }
        } 
        j++;
    }
    outstr[j] = '\0';
}

char* b16tob64(char* input) {
    unsigned inlen = strlen(input);
    unsigned declen = inlen/2;
    unsigned enclen = (declen << 2) / 3 + !!((declen << 2) % 3);

    char decoded[declen+1];
    b16decode(input, decoded, inlen);
    
    char* encoded = (char*) malloc(sizeof(char) * (enclen+1));
    b64encode(decoded, encoded, declen, enclen); 
    return encoded;       
}

int main() {
    char* actual_out = b16tob64(TEST);

    printf("input: %s\n", TEST);
    printf("expected output: %s\n", EXPECTED_OUT);
    printf("actual output: %s\n", actual_out);

    if (strcmp(actual_out, EXPECTED_OUT) == 0) {
        printf("Success!\n");
    }
    else {
        printf("Failure :-(\n");
    }

    free(actual_out);
    return 0;
}