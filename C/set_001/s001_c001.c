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
char* b16 = "0123456789abcdef";
char* b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

char* test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
char* expected_out = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";


/* FUNCTIONS */

// convert hex char to int
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

// decode hex
void b16decode(char* instr, char* outstr, int inlen) {

    char temp1;
    unsigned j = 0;
    for (unsigned i=0; i < inlen; i+=2) {
        temp1 = unhex(instr[i]) * 16 + unhex(instr[i+1]);
        outstr[j] = temp1;
        j++;
    }
    outstr[j] = '\0';
}

// encode b64
void b64encode(char* str);

void b16tob64(char* input) {
    int inlen = strlen(input);

    char decoded[inlen/2 + 1];
    b16decode(input, decoded, inlen);

    // char encoded;

    printf("%s\n", decoded);
}

int main() {
    b16tob64(test);
}