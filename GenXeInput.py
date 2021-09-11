import csv
import pandas as pd
import numpy as np
import os

output = ('./result/output.txt')
path = './result/'
if not os.path.exists(path):
    os.makedirs(path)

f1address = './input/hdf'; f2address = './input/res'
f1 = pd.read_fwf('./input/hdf', index = False, header = None)
f2 = pd.read_fwf('./input/res', index = False, header = None)

locCheck = 0 # ID index
add = [1,2,3] # these are the indeces for the added values
with open(output, 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    i=0
    with open(f1address, "r") as a_file:
      for line in a_file:
        liney = line.strip()
        writer.writerow(np.array([liney]))

        j=0
        with open(f2address, "r") as a_file:
          for line in a_file:
            if(f2.iloc[j,locCheck] == f1.iloc[i,locCheck]):
               string = ''
               for addi in add:
                 string += str(f2.iloc[j,addi])+' '
               writer.writerow(np.array([string]))
            j+=1
        i+=1

#written at Sep 11 2021
