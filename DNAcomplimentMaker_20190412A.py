'''
Author: Luke Hebert
Date begun: 2019 04 12
Description:
	input: string of letters including A's, T's, C's, and G's
	output: reverse of the input string, with all A's replaced with T's,
		C's replaced with G's, and vice versa for both
'''
def getCompliment(nucleotide_str):
    compliment_bp = '.'
    if nucleotide_str in ['G','g']:
        compliment_bp = 'C'
    elif nucleotide_str in ['C','c']:
        compliment_bp = 'G'
    elif nucleotide_str in ['A','a']:
        compliment_bp = 'T'
    elif nucleotide_str in ['T', 't']:
        compliment_bp = 'A'
    else:
        print('Improper nucleotide in DNA template!')
    return compliment_bp

import sys

inFile_path = sys.argv[1]

template_str = ''
with open(inFile_path, 'r') as inFile:
    for line in inFile:
        line = line.replace('\n','')
    template_str += line

complement_str = ''.join([getCompliment(bp) for bp in template_str[::-1]]) #::-1 reverses a string

print('\n' + complement_str)

with open(inFile_path.replace('.txt','_compliment.txt'), 'w') as outFile:
    outFile.write(complement_str)
