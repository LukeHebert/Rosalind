'''
Author: Luke Hebert
Date begun: 2019 04 10
Description:
	input: text file with a string of A's, C's, G's, and T's
	output: text file with 4 digits: the number of A's, C's, G's and T's in that order
'''
import sys

inFile_path = sys.argv[1]

a_int, c_int, g_int, t_int = 0, 0, 0, 0

with open(inFile_path, 'r') as inFile: 
    for line in inFile:
        lineA_int = line.count('A') + line.count('a')
        lineC_int = line.count('C') + line.count('c')
        lineG_int = line.count('G') + line.count('g')
        lineT_int = line.count('T') + line.count('t')
        a_int += lineA_int
        c_int += lineC_int
        g_int += lineG_int
        t_int += lineT_int

print(str(a_int) + ' ' + str(c_int) + ' ' + str(g_int) + ' ' + str(t_int))

with open('ACGT_counts.txt', 'w') as outFile:
    outFile.write(str(a_int) + ' ' + str(c_int) + ' ' + str(g_int) + ' ' + str(t_int))
        
