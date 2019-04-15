'''
Author: Luke Hebert
Date begun: 2019 04 12
Description:
	input
		a text file with three integers separated by spaces
		first number = homozygous dominant individnuals
		second number = heterozygous individuals
		third = homozygous recessive individuals
	output
		probability that two randomly selected individuals would produce an
		offspring who possesses the dominant phenotype
'''

import sys

in_filepath = sys.argv[1]

hardy_str = ''
with open(in_filepath, 'r') as in_file:
    hardy_str = in_file.read().strip('\n\r')

hardy_list = [float(num) for num in hardy_str.split(' ')]
print(hardy_list)
hd, ht, hr, t = hardy_list[0], hardy_list[1], hardy_list[2], sum(hardy_list)
print('You entered \n\tHomozygous Dominant Individuals: %d\n\tHeterozygous Individuals: %d\n\tHomozygous Recessive Individuals: %d')%(int(hd),int(ht),int(hr))
print('\tTotal individuals: ' + str(int(t)))

pDom_list = []

#the probability of a dominant phenotype from a 0/0 x 0/0 cross is always 0

#P(dominant) from 0/0 x 0/1
pDom_list.append( ((hr/t)*(ht/(t-1)))*(0.5) )

#P(dominant) from 0/0 x 1/1
pDom_list.append((hr/t)*(hd/(t-1)))

#P(dominant) from 0/1 x 0/0
pDom_list.append( ((hr/t)*(ht/(t-1)))*(0.5) )

#P(dominant) from 0/1 x 0/1
pDom_list.append( ((ht/t)*((ht-1)/(t-1)))*(0.75) )

#P(dominant) from 0/1 x 1/1
pDom_list.append((ht/t)*(hd/(t-1)))

#P(dominant) from 1/1 x 0/0
pDom_list.append((hr/t)*(hd/(t-1)))

#P(dominant) from 1/1 x 0/1
pDom_list.append((ht/t)*(hd/(t-1)))

#P(dominant) from 1/1 x 1/1
pDom_list.append((hd/t)*((hd-1)/(t-1)))


pDom_int = sum(pDom_list)

print('\n' + str(pDom_int))

with open(in_filepath.replace('.txt', '') + '_pDom.txt', 'w') as out_file:
    out_file.write(str(pDom_int))
