import numpy as np
import re # required to use re.search for finding index of patterns in a string

def format_float(b):
    b_s = "{:.3f}".format(b)
    if (b < 10): b_s = '0'+b_s
    if (b < 100): b_s = '0'+b_s
    if (b < 1000): b_s = '0'+b_s
    return b_s

def format_float_general(b,desired_digits=4):
    b_s = "{:.3f}".format(b)
    n = (desired_digits-1)-int(np.log10(b))
    b_s = '0'*n + b_s
    return b_s

def format_int(b):
    b_s = str(b)
    if (b < 10): b_s = '0'+b_s
    return b_s

def format_str(s):
    fs = s
    char = '*'
    if len(s)<5:fs=fs+char
    if len(s)<4:fs=fs+char
    if len(s)<3:fs=fs+char
    if len(s)<2:fs=fs+char
    return fs

def formater1(text_org):
    index = 0 # to track where we found variable is in the original text
    text = text_org # a copy of original text so we can modify it
    end = False
    k = -1
    while(end==False):
        k+=1
        patern = re.search('\t(.+?)\t', text)
        if patern: # if you found a pattern use it to define found
            found = patern.group(1)
        else: # otherwise use the rest of the text_org as the found pattern
            found = text_org[index:]
            end = True
        found_index = text.find(found)
        text = text[found_index+len(found):]
        if(k!=0): # since we don't want the first find to be replaced
            if(k>4):
                replacement = str(format_float(float(found)))
            else:
                replacement = str(format_int(int(found)))
            text_org = text_org[:index+1]+replacement+text_org[index+1+len(found):]
            index += len(replacement)-len(found) # we modified the text so its long
        index += found_index+len(found)
    return text_org

def formater2(text_org):
    index = 0 # to track where we found variable is in the original text
    text = text_org # a copy of original text so we can modify it
    end = False
    k = -1
    while(end==False):
        k+=1
        bgn = -1
        fin = -1
        ik = -1
        this_end = False
        while(not this_end and ik < len(text)-1):
            ik += 1
            if (text[ik]==' ' and bgn==-1):
                bgn = ik+1
                fin = ik+1
            elif(text[ik]==' '):
                fin = ik
                this_end = True
        patern = text[bgn:fin]
        if patern: # if you found a pattern use it to define found
            found = patern
        else: # otherwise use the rest of the text_org as the found pattern
            found = text_org[index+1:]
            print('index',index)
            print('found',found)
            end = True
        found_index = text.find(found)
        text = text[found_index+len(found):]
        index += found_index
        if(k>1):
            replacement = str(format_float(float(found)))
        else:
            replacement = str(format_str(found))
        text_org = text_org[:index]+replacement+text_org[index+len(found):]
        index += len(replacement) # we modified the text so its long

    return text_org

def main():
    '''
    a = 2.3
    print(format_float_general(a))

    text_org = '603879074	2014	6	2	18	09	  45	 19.9999	  45	  45	  45'
    print(formater1(text_org))
    '''

    text_org = 'ISC FUG Pn 15.62 0.7521 5 0.6 09'
    print(text_org)
    print(formater2(text_org))
main()
