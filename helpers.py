import os
from collections import deque
from math import exp
from keras.layers import Dense, Input, Masking, BatchNormalization, Layer, Embedding, Dropout
from keras.layers import LSTM, Reshape, TimeDistributed, Concatenate, Multiply, RepeatVector
from keras import Model
from keras import backend as K
import numpy as np
import h5py
import requests
import string
import pickle
import pandas as pd

def input_processer(seqs_path, dict_path):
    jokes_path = "DataJokes/input.txt"

    input_file = open(jokes_path, "r").read()
    jokes = input_file.split('\n')
    jokes = np.random.shuffle(np.array(jokes))

    #pre make dict
    char_dict = {"<BOUND>":0}
    for ix, char in enumerate(string.printable):
        if char not in ('\x0c', '\x0b', "\r"):
            char_dict[char] = ix+1

    #now save the character dict
    pickle_out = open(dict_path,"wb")
    pickle.dump(char_dict, pickle_out)
    pickle_out.close()

    f = h5py.File(seqs_path, 'w')
    dt = h5py.special_dtype(vlen=np.dtype('int32'))
    dset = f.create_dataset('seqs', (len(jokes),), dtype=dt)
    for i in range(len(jokes)):
        text=jokes[i]
        #make certain all strings
        seq = [char_dict["<BOUND>"]]
        for char in text:
            if char in string.printable:
                try:
                    seq.append(char_dict[char])
                except KeyError:
                    pass
        dset[i]=np.array(seq, dtype="int32")
