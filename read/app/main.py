import os
from os.path import exists
from pathlib import Path
from settings import DATAFOLDER
from settings import FILENAME

def read():

    datapath = os.path.join(Path(__file__).parents[1], DATAFOLDER)

    if exists(os.path.join(datapath, FILENAME + '.txt')):
        print('DATAFOLDER contains', os.listdir(datapath))
        print('Content of the file is:')
        with open(os.path.join(datapath, FILENAME+'.txt'), 'r') as f:
            lines = f.readlines()
            print(lines)
    else:
        print('File does not exist: ',os.path.join(datapath, FILENAME + '.txt'))

if __name__ == '__main__':

    read()