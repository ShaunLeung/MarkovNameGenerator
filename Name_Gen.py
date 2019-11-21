import pandas as pd
import random

f = open("Raw_Data.txt",'r')


def build_data_base(data,n):
    chain = {
        '_start':{},
        '_names': set(data)
    }

    for name in data:
        word_wrapped = str(name) + '.'
        for i in range(0,word_wrapped - n):
            tuple = word_wrapped[i:i+n]
            next = word_wrapped[i+1:i+1]
        
            if tuple not in chain:
                entry = chain[tuple] = {}
            else:
                entry = chain[tuple]

            if i ==0:
                if tuple not in chain[tuple]:
                    chain['_start'][tuple] = 1
                else:
                    chain['_start'][tuple] += 1
            
            if next not in entry:
                entry[next] = 1
            else:
                entry[next] += 1

    return chain