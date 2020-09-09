/* File name: s001_c002.c
 * Description: Cryptopals Set 1, Challenge 2 - Fixed XOR
 * Author: Arya Muralidharan
 * Date: 2020-09-07 */


/* LIBRARIES */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* CONSTANTS */
char* INPUT_1 = "1c0111001f010100061a024b53535009181c";
char* INPUT_2 = "686974207468652062756c6c277320657965";
char* EXPECTED_OUT = "746865206b696420646f6e277420706c6179";


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

// b16encode: encode hex
void b16encode(char* instr, char* outstr, unsigned inlen) {
    char* b16 = "0123456789abcdef";

    for (unsigned i=0; i<inlen; i++) {
		outstr[i*2]   = b16[instr[i] >> 4];
		outstr[i*2+1] = b16[instr[i] & 0xF];
	}
	outstr[inlen*2+1] = '\0';
}


char* fixed_xor(char* str1, char* str2) {
    unsigned inlen = strlen(str1);

    char b_str1[inlen/2+1];
    b16decode(str1, b_str1, inlen);
    char b_str2[inlen/2+1];
    b16decode(str2, b_str2, inlen);

    char xord[inlen/2+1], temp;
    unsigned i;

    for (i = 0; i < inlen/2; i++) {
        temp = (b_str1[i] ^ b_str2[i]);
        xord[i] = temp;
    }
    xord[i] = '\0';

    char* reenc = (char*) malloc(sizeof(char) * (inlen+1));
    b16encode(xord, reenc, inlen/2);    

    return reenc;       
}


int main() {
    
    char* actual_out = fixed_xor(INPUT_1, INPUT_2);

    printf("input 1: %s\n", INPUT_1);
    printf("input 2: %s\n", INPUT_2);
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