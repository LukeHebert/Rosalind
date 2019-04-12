'''
Author: Luke Hebert
Date begun: 2019 04 10
Description:
	input: a .txt file containing a string of any combination of G,A,T, & C
	output: a .txt file containing a string of the corresponding RNA letters G, A, U, & C
'''

import sys
import os

slash = '/'
if os.name == 'nt':
    slash = '\\'

inFile_path = sys.argv[1]

rna_str = ''

with open(inFile_path, 'r') as inFile:
    for line in inFile:
        rna_str += line.strip('\n').replace('T','U').replace('t','u')

outFile_name = inFile_path.split(slash)[-1].replace('.txt','') + '_RNA.txt'
with open(outFile_name, 'w') as outFile:
    outFile.write(rna_str)
