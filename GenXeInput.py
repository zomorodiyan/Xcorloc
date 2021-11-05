import csv
import pandas as pd
import numpy as np
import os
import time
from format_tools import formater1, formater2

output = ('./result/output.txt')
path = './result/'
if not os.path.exists(path):
    os.makedirs(path)

f1address = './data/'; f2address = './data/'

###HDF data
colspecs = [(0, 1), (1, 4), (4, 5), (5, 6), (6, 8), (8, 11), (11 ,14), (15, 19), (19, 22),
        (22, 27), (27, 36), (36, 45), (45, 51), (51, 57), (57, 61), (61, 65),(65, 69),
        (69, 73), (73, 77), (77, 81), (81, 85), (85, 93), (93, 101), (101, 109),(109, 115),
        (115, 121), (121, 127), (127, 131), (131, 135), (135, 139), (139, 143), (143, 148), (147, 157)]

f1 = pd.read_csv(f1address + '2014_myarea.hdf', delimiter = '\t' , header = None )
f1.iloc[:,4] = '20' + f1.iloc[:,4].astype(str) ### changing year format from 14 to 2014
quake_info = f1.iloc[:, [32, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]]
quake_info.to_csv(f1address + '2014_XCinp.hdf', header = 0, sep = '\t', index = False, float_format = '%8.3f')
f1 = pd.read_csv(f1address + '2014_XCinp.hdf', delimiter = '\t', header = None)

###RES data
f2 = pd.read_csv(f2address + '2014_myareaphtest1.res', delimiter = '\t', header = None)
#print(f2) ;print(len(f2.columns))
###adding a new column to the DataFrame from right. The index of this new column: 54
f2[len(f2.columns)] = 'ISC'
#print(f2) ;print(len(f2.columns))


###creating input in the format of XCORLOC/phaselist.in
locCheck = 0 # ID index
ievt_res = 53
add = [54, 20, 28, 37, 24] # these are the indeces for the added values (sta, phase, tt, dist)



with open(output, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    i=0
    with open(f1address + '2014_XCinp.hdf', 'r') as a_file:
      for line in a_file:
        liney = line.strip()
        #print([liney])
        liney = formater1(liney)
        #print([liney])

        writer.writerow(np.array([liney]))


        j=0
        with open(f2address + '2014_myareaphtest1.res', 'r') as a_file:
          for line in a_file:
            if(f2.iloc[j, ievt_res] == f1.iloc[i,locCheck]):
               string = ''
               for addi in add:
                 string += str(f2.iloc[j,addi])+' '
               #print([string])
               string = formater2(string[:-1])
               #print([string])
               time.sleep(1)
               #q = writer.writerow(np.array([string]))
               #print(q)
            j+=1
        i+=1

#print(f2.iloc[:, [54, 20, 28, 37, 24]].dtypes)
#r = f2.iloc[:,[ 54, 20, 28]]

#written at Sep 11 2021
#modified at Nov 04 2021
